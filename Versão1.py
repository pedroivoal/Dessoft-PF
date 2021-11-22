import pygame
import random

pygame.init()

# -- Tela inicial
largura = 1200
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space run')


# -- inicio do jogo

largura_aviao = 200
altura_aviao = 100
largura_nave = 50
altura_nave = 250
font = pygame.font.SysFont(None, 48)

background = pygame.image.load('imagem1.png').convert()
background = pygame.transform.scale(background,(largura,altura))

image_aviao = pygame.image.load('aviao.png').convert()
image_aviao = pygame.transform.scale(image_aviao,(largura_aviao,altura_aviao))

image_nave = pygame.image.load('Shuttle.png').convert()
image_nave = pygame.transform.scale(image_nave,(largura_nave,altura_nave))

# -- estrutura dos dados

class nave(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class aviao(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura-largura_aviao)
        self.rect.y = random.randint(-100, -altura_aviao)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura-largura,)
            self.rect.y = random.randint(-100, -altura_aviao)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)       
        
# -- ajuste de velocidade
time = pygame.time.Clock()
FPS = 30

# Criando um grupo de avioes
all_sprites = pygame.sprite.Group()
all_avioes = pygame.sprite.Group()

# Criando o jogador
player = nave(image_nave)
all_sprites.add(player)

# Criando os avioes
for i in range(8):
    Aviao = aviao(image_aviao)
    all_sprites.add(Aviao)
    all_avioes.add(Aviao)

# -- Parâmetro para inicio e final do jogo
game = True  

# -- Loop principal

while game:
    # ----- Trata eventos
    for event in pygame.event.get():    # ----- Verifica consequências

        if event.type == pygame.QUIT:
            game = False

        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:

            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:

            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

        # Atualizando a posição dos avioes
        all_sprites.update()

        # Verifica se houve colisão entre nave e um aviao
        hits = pygame.sprite.spritecollide(player, all_avioes, True)

         # ----- Gera saídas
        tela.fill((0,0,0))  # Preenche com a cor branca
        tela.blit(background, (10, 10))

        # Desenhando meteoros
        all_sprites.draw(tela)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados