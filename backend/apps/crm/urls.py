from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProjectViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
