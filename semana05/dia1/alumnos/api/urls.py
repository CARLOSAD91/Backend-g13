from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumnos',views.alumnos),
    path('home',views.home),
    path('getAlumnos',views.getAlumnos),
    path('setAlumno',views.setAlumno),
    path('profesor',views.profesor),
    path('profesor/<int:profesor_id>',views.profesor_detail),
]