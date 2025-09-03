from django.urls import path
from .views import relationship, relationship_detail

urlpatterns = [
    path('', relationship),
    path('<int:pk>/', relationship_detail),
]