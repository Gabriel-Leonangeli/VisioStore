from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('formato/nuevo/', views.crear_formato, name='crear_formato'),
    path('visual/nuevo/', views.crear_visual, name='crear_visual'),
    path('buscar/', views.buscar_visual, name='buscar_visual'),
]

