from django.urls import path
from . import views


urlpatterns = [
    path('generatedata/', views.load_all_from_default),
    path('exportdata/', views.export_models),
    path('show/', views.show_me, name='show'),
    path('formula/', views.show_formula),
    path('formula1/', views.editor_formula),
    path('showresults/', views.show_results)
]
