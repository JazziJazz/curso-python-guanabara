# Programa de computador que roda uma música em MP3 utilizando a biblioteca PyGame.
import pygame

try:
    pygame.mixer.init()
except:
    print('Não foi possível iniciar o mixer do PyGame.')


pygame.mixer.music.load('musica/pygame/lover is a day.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
