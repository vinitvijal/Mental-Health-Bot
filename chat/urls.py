from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page),  # this serves the HTML page
    path('chat/', views.chat_with_bot),
]