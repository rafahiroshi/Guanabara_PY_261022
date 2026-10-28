import pygame

pygame.init()
pygame.mixer.music.load('M1/minhaFelicidadeLofi.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()