from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProjectViewSet, CategoryViewSet, get_contact_form, send_project_link, public_project_view

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('contacto/', get_contact_form, name='contacto'),
    path('project/send-link/<int:project_id>/', send_project_link, name='send_project_link'),
    path('project/public/<uuid:token>/', public_project_view, name='public_project_view'),
    path('project/public/<uuid:token>/accept/', public_accept_terms, name='public_accept_terms'),
    path('', include(router.urls)),
]
