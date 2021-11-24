# Todas bibliotecas do programa
import pygame
import random

pygame.init()

# Tela principal
window_width = 1000
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Run')
font = pygame.font.SysFont(None, 48)

plane_width = 100
plane_heigth = 80
nave_width = 20
nave_heigth = 40

elements = {}
elements['background1'] = pygame.image.load(r'imagem1.png').convert()
elements['background1'] = pygame.transform.scale(elements['background1'], (window_width, window_height))
elements['plane'] = pygame.image.load(r'aviao.png').convert_alpha()
elements['plane'] = pygame.transform.scale(elements['plane'], (nave_width, nave_heigth))

class Plane(pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-100, 0-plane_width)
        self.rect.y = random.randint(0, window_height-plane_heigth)
        self.speedx = random.randint(2, 8)
        self.speedy = 0

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > window_width:
            self.rect.x = random.randint(-100, 0-plane_width)
            self.rect.y = random.randint(0, window_height-plane_heigth)
            self.speedx = random.randint(2, 8)
            self.speedy = 0



game = True

clock = pygame.time.Clock()
FPS = 30

plane1 = Plane(elements['plane'])

while game:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
    
    plane1.update()

    window.fill((0, 0, 0))
    window.blit(elements['background1'], (0, 0))

    window.blit(plane1.image, plane1.rect)

    pygame.display.update()

pygame.quit()