import pygame
import random

pygame.init()

# -- Tela inicial
largura = 1200
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Space run')


# -- inicio do jogo

largura_aviao = 150
altura_aviao = 100
largura_nave = 100
altura_nave = 200
font = pygame.font.SysFont(None, 48)

background = pygame.image.load('imagem1.png').convert()
background = pygame.transform.scale(background,(largura,altura))

image_aviao = pygame.image.load('aviaoguerra.png').convert_alpha()
image_aviao = pygame.transform.scale(image_aviao,(largura_aviao,altura_aviao))

image_nave = pygame.image.load('Shuttle.png').convert_alpha()
image_nave = pygame.transform.scale(image_nave,(largura_nave,altura_nave))

# -- estrutura dos dados

class nave(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura /2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > altura:
            self.rect.bottom = altura

class aviao(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura-largura_aviao)
        self.rect.y = random.randint(1, 800)
        self.speedx = 1
        self.speedy = 0

    def update(self):
        # Atualizando a posição do aviao
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Se o aviao passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.x = 0
    
            ## self.speedx = random.randint(3, 10)
            ## self.speedy = random.randint(2, 15)       
        
# -- ajuste de velocidade
time = pygame.time.Clock()
FPS = 0

# Criando um grupo de avioes
all_sprites = pygame.sprite.Group()
all_avioes = pygame.sprite.Group()

# Criando o jogador
player = nave(image_nave)
all_sprites.add(player)

# Criando os avioes
for i in range(5):
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
                player.speedx -= 4
            if event.key == pygame.K_RIGHT:
                player.speedx += 4
            if event.key == pygame.K_DOWN:
                player.speedy += 4
            if event.key == pygame.K_UP:
                player.speedy -= 4

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:

            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 4
            if event.key == pygame.K_RIGHT:
                player.speedx -= 4
            if event.key == pygame.K_DOWN:
                player.speedy -= 4
            if event.key == pygame.K_UP:
                player.speedy += 4

    # Atualizando a posição dos avioes
    all_sprites.update()

    # Verifica se houve colisão entre nave e um aviao
    hits = pygame.sprite.spritecollide(player, all_avioes, True)

    if hits == True:
        game = False

        # ----- Gera saídas
    tela.fill((0,0,0))  # Preenche com a cor branca
    tela.blit(background, (10, 10))

    # Desenhando meteoros
    all_sprites.draw(tela)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados