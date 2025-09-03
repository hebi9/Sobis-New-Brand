from django.shortcuts import render
from .models import Services
from django.http import JsonResponse

# Create your views here.
def services_view(request):
    services = Services.objects.all()
    return JsonResponse({
        'success': True,
        'services': services,
    }, status=200)