from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('submit_event/', views.submit_event, name='submit_event'),
]
