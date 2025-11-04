from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('formato/nuevo/', views.crear_formato, name='crear_formato'),
    path('visual/nuevo/', views.crear_visual, name='crear_visual'),
    path('buscar/', views.buscar_visual, name='buscar_visual'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
