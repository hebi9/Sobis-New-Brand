from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Customer, Project, Category
from .serializers import CustomerSerializer, ProjectSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.urls import reverse



User = get_user_model()

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by("-created_at")
    serializer_class = CustomerSerializer

    # Búsqueda y filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        "sobis_user",
        "sobis_username",
        "name",
        "email",
        "phone",
        "state",
        "country",
        "created_at",
        "updated_at",
    ]
    search_fields = ["sobis_username", "name", "email", "phone"]
    ordering_fields = ["created_at", "updated_at", "name"]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("status", "-created_at")
    serializer_class = ProjectSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        "name",
        "customer",
        "customer__sobis_user",
        "accepted_terms",
        "categories",
        "created_at",
        "updated_at",
    ]
    search_fields = ["name", "customer__name", "customer__sobis_username"]
    ordering_fields = ["created_at", "updated_at", "status", "name"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name", "created_at", "updated_at"]


def public_project_view(request, token):
    project = get_object_or_404(Project, token=token)
    serializer = ProjectSerializer(project)
    return JsonResponse(serializer.data)

@csrf_exempt
@require_http_methods(["PATCH"])
def public_accept_terms(request, token):
    try:
        project = Project.objects.get(token=token)

        data = json.loads(request.body)
        accepted = data.get("accepted_terms", False)

        if accepted:
            project.accepted_terms = True
            project.accepted_at = now()
            project.save()
            return JsonResponse({"message": "Términos aceptados"}, status=200)
        else:
            return JsonResponse({"error": "Campo 'accepted_terms' requerido como true"}, status=400)

    except Project.DoesNotExist:
        return JsonResponse({"error": "Proyecto no encontrado"}, status=404)
    except Exception as e:
        return JsonResponse({"error": f"Error: {str(e)}"}, status=500)

@csrf_exempt
def get_contact_form(request):
    if request.method == "POST":
        try:
            print(User.objects.get(username="sobis"))
            data = json.loads(request.body)
            customer = Customer.objects.create(
                sobis_user=User.objects.get(username="sobis"),  # Usuario por defecto
                name=data.get("nombre"),
                email=data.get("correo"),
            )
            print(customer)
            project=Project.objects.create(
                name=data.get("asunto"),
                description=data.get("descripcion"),
                customer=customer
            )
            send_email(data.get("nombre"),data.get("asunto"),data.get("correo"),data.get("descripcion"),request)

            return JsonResponse({"message": "Datos recibidos correctamente"}, status=200)
        except Exception as e:
            print("❌ Error procesando datos:", str(e))
            return JsonResponse({"error": "Error procesando datos"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


def send_email(nombre,asunto,correo,descripcion, request):
    email_subject = nombre + " - " + asunto
    # sirve para ignorar etiquetas html
    mensaje_texto = f"{nombre}  \n{asunto} \nresponder a: {correo}\n{descripcion}"
    try:
        send_mail(email_subject, mensaje_texto, correo,
                  ["faoa.16@gmail.com"])

    except Exception:
        print("error al enviar correo")



@csrf_exempt
def send_project_link(request, project_id):
    if request.method == "POST":
        try:
            project = get_object_or_404(Project, id=project_id)

            # Asegurarse que tiene token (por si se migraron datos viejos sin token)
            if not project.token:
                import uuid
                project.token = uuid.uuid4()
                project.save()

            # Construir URL absoluta
            link = request.build_absolute_uri(
                reverse('public_project_view', kwargs={'token': str(project.token)})
            )

            subject = f"Detalles de tu proyecto: {project.name}"
            message = f"""
Hola {project.customer.name},

Gracias por tu interés. Puedes ver los detalles de tu proyecto y aceptar los términos y condiciones en el siguiente enlace:

{link}

Si tienes alguna duda, no dudes en contactarnos.

Atentamente,
Equipo de Sobi's Dev
            """

            send_mail(subject, message, "noreply@sobis.com", [project.customer.email])
            return JsonResponse({"message": "Correo enviado correctamente."}, status=200)

        except Exception as e:
            print("❌ Error enviando correo:", e)
            return JsonResponse({"error": "No se pudo enviar el correo."}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
