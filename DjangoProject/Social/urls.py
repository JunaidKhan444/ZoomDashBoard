from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.DisplayPosts.as_view()),
    path('ig/', views.IgData.as_view()),
]