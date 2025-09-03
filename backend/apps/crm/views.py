from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, Project, Category
from .serializers import CustomerSerializer, ProjectSerializer, CategorySerializer


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
