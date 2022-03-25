from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.DisplayMeetings.as_view(),name = 'meetings'),
    path('delete/<str:pk>/', views.deletemeeting,name = 'delete'),
    path('create/',views.addmeeting,name = 'add'),
    path('edit/<str:pk>/',views.editmeeting, name='edit')

]