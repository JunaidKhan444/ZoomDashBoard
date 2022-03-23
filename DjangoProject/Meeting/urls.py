from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.DisplayMeetings.as_view(),name = 'meetings'),
    path('delete/<str:pk>/', views.deletemeeting,name = 'delete')

]