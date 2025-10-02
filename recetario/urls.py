from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/', views.recetas, name='recetas'),
    path('contacto/', views.contacto, name='contacto'),
    path('recetas/<int:receta_index>/', views.detalle_receta, name='detalle_receta'),
    path('eventos/nuevo', views.nuevo_evento, name='nuevo_evento'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/exitoso', views.evento_exitoso, name='evento_exitoso'),
]