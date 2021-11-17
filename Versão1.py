import pygame
import random


pygame.init()

# -- Tela inicial
tela = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Mars')

# -- Estrutura inicial do jogo

game = True

# -- Loop principal

while game:
    # ----- Trata eventos
    for event in pygame.event.get():    # ----- Verifica consequências

        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    tela.fill((255, 255, 255))  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados