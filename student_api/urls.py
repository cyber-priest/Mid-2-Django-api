from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStudent),
    path('add/', views.setStudent),
    path('update/<str:pk>/', views.updateStudent),
    path('delete/<str:pk>/', views.deleteStudent)
]