from django.urls import path

from . import views

urlpatterns = [
    path('', views.quotes_view, name='services_view'),
]
