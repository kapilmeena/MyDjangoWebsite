from django.urls import path
from . import views


urlpatterns = [
    path('generatedata/', views.load_all_from_default),
    path('exportdata/', views.export_models),
]
