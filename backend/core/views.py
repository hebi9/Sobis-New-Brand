from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, get_object_or_404
from .models import Page, WhoWeAre, Methodology

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):
    return Response({"message": f"Hola {request.user.username}, bienvenido al dashboard."})

def robots_txt(request):
    content = "User-agent: *\nDisallow:\nSitemap: http://localhost:8000/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def who_we_are(request):
    who_we_are = WhoWeAre.objects.all()
    return JsonResponse({
        'success': True,
        'who_we_are': list(who_we_are.values()),
    }, status=200)

def methodology(request):
    methodology = Methodology.objects.all()
    return JsonResponse({
        'success': True,
        'methodology': list(methodology.values()),
    }, status=200)