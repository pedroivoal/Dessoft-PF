import pygame
import random


pygame.init()

# -- Tela inicial
largura = 600
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space run')

# -- Estrutura inicial do jogo

game = True

# -- Imagem de inicio
image = pygame.image.load('GitHub\Dessoft-PF\mars1.png').convert()

# -- Loop principal

while game:
    # ----- Trata eventos
    for event in pygame.event.get():    # ----- Verifica consequências

        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    tela.fill((0,0,0))  # Preenche com a cor branca
    tela.blit(image, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados