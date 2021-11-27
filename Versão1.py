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

assets = {}
assets['background'] = pygame.image.load('imagem1.png').convert()
assets['background']= pygame.transform.scale(assets['background'],(largura,altura))

assets['image_aviao'] = pygame.image.load('caça.png').convert_alpha()
assets['image_aviao'] = pygame.transform.scale(assets['image_aviao'],(largura_aviao,altura_aviao))

assets['image_nave'] = pygame.image.load('Shuttle.png').convert_alpha()
assets['image_nave'] = pygame.transform.scale(assets['image_nave'],(largura_nave,altura_nave))

anim_explosao = []

for i in range(9):
    # arquivos da animacao
    animacao = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(animacao).convert()
    img = pygame.transform.scale(img, (72, 72))
    anim_explosao.append(img)
assets["anim_explosao"] = anim_explosao

# -- estrutura dos dados

class nave(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randint(-1000, 0-largura_aviao)
        self.rect.y = random.randint(0, altura-altura_aviao)
        self.speedx = 5
        self.speedy = 0

    def update(self):
        # Atualizando a posição do aviao
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Se o aviao passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.x = random.randint(-1000, 0-largura_aviao)
            self.rect.y = random.randint(0, altura-altura_aviao)
            self.speedx = random.randint(2, 8)
            self.speedy = 0

    
class Explosao(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):

        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.anim_explosao = assets['anim_explosao']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.anim_explosao[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.anim_explosao):
                self.kill()

            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.anim_explosao[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
        
# -- ajuste de velocidade
time = pygame.time.Clock()
FPS = 60

# Criando um grupo de avioes
all_sprites = pygame.sprite.Group()
all_avioes = pygame.sprite.Group()

# Criando o jogador
player = nave(assets['image_nave'])
all_sprites.add(player)

# Criando os avioes
for i in range(5):
    Aviao = aviao(assets['image_aviao'])
    all_sprites.add(Aviao)
    all_avioes.add(Aviao)

# -- Parâmetro para inicio e final do jogo
game = True  
lives = 3

# -- Loop principal
while game:
    time.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():    # ----- Verifica consequências

        if event.type == pygame.QUIT:
            game = False

        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:

            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 15
            if event.key == pygame.K_RIGHT:
                player.speedx += 15
            if event.key == pygame.K_DOWN:
                player.speedy += 15
            if event.key == pygame.K_UP:
                player.speedy -= 15

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:

            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 15
            if event.key == pygame.K_RIGHT:
                player.speedx -= 15
            if event.key == pygame.K_DOWN:
                player.speedy -= 15
            if event.key == pygame.K_UP:
                player.speedy += 15

    # Atualizando a posição dos avioes
    all_sprites.update()

    # Verifica se houve colisão entre nave e um aviao
    hits = pygame.sprite.spritecollide(player, all_avioes, True, pygame.sprite.collide_mask)

    # explosao dos avioes
    for aviao in hits:
        explosao = Explosao(aviao.rect.center, assets)
        all_sprites.add(explosao)

    
    if hits:
       lives -= 1

    if lives == 0:
        game = False
        time.sleep(100)

        # ----- Gera saídas
    tela.fill((0,0,0))  # Preenche com a cor branca
    tela.blit(assets['background'], (10, 10))

    # Desenhando meteoros
    all_sprites.draw(tela)

    # Desenhando as vidas
    #text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 0, 0))
    #text_rect = text_surface.get_rect()
    #text_rect.bottomleft = (10, altura - 10)
    #tela.blit(text_surface, text_rect)


    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados