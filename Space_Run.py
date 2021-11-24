# Todas bibliotecas do programa
import pygame
import random

pygame.init()

# Tela principal
window_width = 900
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Run')

plane_width = 50
plane_heigth = 30
nave_width = 20
nave_heigth = 40


elements = {}
elements['background1'] = pygame.image.load(r'imagem1.png').convert()
elements['background1'] = pygame.transform.scale(elements['background1'], (window_width, window_height)).convert()

game = True

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        

    window.fill((0, 0, 0))
    window.blit(elements['background1'], (0, 0))

    pygame.display.update()
