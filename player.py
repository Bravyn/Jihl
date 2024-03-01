import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

file_path = "sinmidele_come.mp3"
play_music(file_path)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)