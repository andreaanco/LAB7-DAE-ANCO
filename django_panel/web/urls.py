from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
 path('', views.AlumnoView.as_view(),name='index'),
 path('profesor/', views.ProfesorView.as_view(),name='profesores')]