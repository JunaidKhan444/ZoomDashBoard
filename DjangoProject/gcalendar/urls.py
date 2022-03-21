from django.urls import path
from . import views

urlpatterns = [
    path('oauth/', views.auth),
    path('', views.get_token),
]