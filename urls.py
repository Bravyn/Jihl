from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.play_music, name='play_music'),
    path('stop/', views.stop_music, name='stop_music'),

]