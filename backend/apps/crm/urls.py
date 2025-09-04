from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProjectViewSet, CategoryViewSet, get_contact_form

router = DefaultRouter()
router.register(r'customers/', CustomerViewSet)
router.register(r'projects/', ProjectViewSet)
router.register(r'categories/', CategoryViewSet)

urlpatterns = [
    path('contacto/', get_contact_form, name='contacto'),
    path('', include(router.urls)),
]
