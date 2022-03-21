from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.DisplayMeetings.as_view()),

]