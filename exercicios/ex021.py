import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("seu_arquivo.mp3")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Reprodução concluída!")
