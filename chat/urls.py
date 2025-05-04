from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page),  
    path('api/', views.chat_with_bot),
]