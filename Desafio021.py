#Permite tocar uma música que esteja no mesmo projeto que o arquivo python
import pygame
pygame.init() #inicia o pygame
pygame.mixer.music.load('arquivo da música') #carrega a música
pygame.mixer.music.play()
pygame.event.wait()
