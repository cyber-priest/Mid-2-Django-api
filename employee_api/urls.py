from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEmployee),
    path('add/', views.setEmployee),
    path('delete/<str:pk>/', views.deleteEployee),
]