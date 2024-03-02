from django.shortcuts import render
from django.http import HttpResponse

import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    return HttpResponse("Music is playing")

def stop_music(request):
    pygame.mixer.music.stop()
    return HttpResponse("Music stopped")


file_path = "sinmidele_come.mp3"
play_music(file_path)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)