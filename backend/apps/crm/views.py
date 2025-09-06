from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Customer, Project, Category
from .serializers import CustomerSerializer, ProjectSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


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