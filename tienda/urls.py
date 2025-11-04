from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('formato/nuevo/', views.crear_formato, name='crear_formato'),
    path('visual/nuevo/', views.crear_visual, name='crear_visual'),
    path('visual/mis/', views.mis_visuales, name='mis_visuales'),
    path('visual/<int:visual_id>/editar/', views.editar_visual, name='editar_visual'),
    path('visual/<int:visual_id>/eliminar/', views.eliminar_visual, name='eliminar_visual'),
    path('buscar/', views.buscar_visual, name='buscar_visual'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
