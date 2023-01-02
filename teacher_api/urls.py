from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTeacher),
    path('add/', views.setTeacher),
    path('delete/<str:pk>/', views.deleteTeacher),
]