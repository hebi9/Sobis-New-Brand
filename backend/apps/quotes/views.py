from django.shortcuts import render
from .models import Quotes
from django.http import JsonResponse

# Create your views here.
def quotes_view(request):
    quotes = Quotes.objects.all()
    return JsonResponse({
        'success': True,
        'quotes': quotes,
    }, status=200)
