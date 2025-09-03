from django.urls import path,include
from .views import dashboard_data, page_detail, who_we_are, methodology

urlpatterns = [
    path('dashboard/', dashboard_data),
    path('who-we-are/', who_we_are),
    path('methodology/', methodology),
    path('services/', include('apps.services.urls')),
    path('quotes/', include('apps.quotes.urls')),
    path('finances/', include('apps.finances.urls')),
    path('relationship/', include('apps.relationship.urls')),
    path('crm/', include('apps.crm.urls')),
    path('<slug:slug>/', page_detail, name='page_detail'),#este es para las páginas estáticas - va al final
]
