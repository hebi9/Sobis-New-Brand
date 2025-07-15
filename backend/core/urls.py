from django.urls import path
from .views import dashboard_data, page_detail

urlpatterns = [
    path('dashboard/', dashboard_data),
    path('<slug:slug>/', page_detail, name='page_detail'),

]
