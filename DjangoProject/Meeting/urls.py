from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.DisplayMeetings.as_view(),name = 'meetings'),
    path('delete/<str:pk>/', views.deletemeeting.as_view(),name = 'delete'),
    path('create/',views.addmeeting.as_view(),name = 'add'),
    path('edit/<str:pk>/',views.editmeeting.as_view(), name='edit')

]