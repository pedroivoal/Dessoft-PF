import pygame
import random

pygame.init()
pygame.mixer.init()

# -- Tela inicial
largura = 1200
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('MARS')


# -- inicio do jogo

largura_aviao = 120
altura_aviao = 120
largura_nave = 40
altura_nave = 160
font = pygame.font.SysFont(None, 48)

assets = {}
# background do jogo
assets['background'] = pygame.image.load(r'img\spacebg.jpg').convert()
assets['background']= pygame.transform.scale(assets['background'],(largura,altura))

# tela inicial
assets['tela_init'] = pygame.image.load(r'img\screen_start1.png').convert()
assets['tela_init']= pygame.transform.scale(assets['tela_init'],(largura,altura))

# tela do gameover
assets['tela_fin'] = pygame.image.load(r'img\screen_gameover1.png').convert()
assets['tela_fin']= pygame.transform.scale(assets['tela_fin'],(largura,altura))

# imagem do ufo
assets['image_aviao'] = pygame.image.load(r'img\ufo2.png').convert_alpha()
assets['image_aviao'] = pygame.transform.scale(assets['image_aviao'],(largura_aviao,altura_aviao))

# imagem da nave 1 do jogador
assets['image_nave'] = pygame.image.load(r'img\ITS1.png').convert_alpha()
assets['image_nave'] = pygame.transform.scale(assets['image_nave'],(largura_nave,altura_nave))
# imagem da nave 2 do jogador
assets['image_nave2'] = pygame.image.load(r'img\ITS2.png').convert_alpha()
assets['image_nave2'] = pygame.transform.scale(assets['image_nave2'],(largura_nave,altura_nave))

# Carrega os sons do jogo
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(loops=-1)

# fim de jogo
gameover = 0

# tela inicial
start = 1

# durante o jogo
playing = 2

# estado atual
state = start

# sair do jogo na hora
over = 3

while state == start:
    tela.fill((0,0,0))  # Preenche com a cor branca
    tela.blit(assets['tela_init'], (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            state = playing

        if event.type == pygame.QUIT:
            state = over          
    pygame.display.update()                                                        

anim_explosao_av = []
anim_explosao_nav = []

for i in range(9):
    # arquivos da animacao
    animacao = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(animacao).convert()
    img = pygame.transform.scale(img, (72, 72))
    anim_explosao_av.append(img)
assets["anim_explosao_av"] = anim_explosao_av

for i in range(9):
    # arquivos da animacao
    animacao = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(animacao).convert()
    img = pygame.transform.scale(img, (150, 150))
    anim_explosao_nav.append(img)
assets["anim_explosao_nav"] = anim_explosao_nav

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

class Aviao(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-1000, 0-largura_aviao)
        self.rect.y = random.randint(0, altura-altura_aviao)
        self.speedx = random.randint(2, 4)
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
            self.speedx = random.randint(2+int(pygame.time.get_ticks()/100)//200, 4+int(pygame.time.get_ticks()/100)//200)
            self.speedy = 0

    
class Explosao(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):

        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.anim_explosao = assets['anim_explosao_av']

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

class Explosao2(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):

        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.anim_explosao_nav = assets['anim_explosao_nav']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.anim_explosao_nav[self.frame]  # Pega a primeira imagem
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
            if self.frame == len(self.anim_explosao_nav):
                self.kill()

            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.anim_explosao_nav[self.frame]
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
score = 0

# Criando os avioes
for i in range(7):
    aviao = Aviao(assets['image_aviao'])
    all_sprites.add(aviao)
    all_avioes.add(aviao)

front_score = pygame.font.Font('PressStart2P.ttf', 28)

# -- Parâmetro para inicio e final do jogo
game = True
lives = 3
i = 0
# -- Loop principal
while state == playing:
    time.tick(FPS)
    
    if score%2500 == 0 and score != 0:
        lives += 1

    # ----- Trata eventos
    for event in pygame.event.get():    # ----- Verifica consequências

        if event.type == pygame.QUIT:
            state = over

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
        explosao2 = Explosao2(player.rect.center, assets)
        all_sprites.add(explosao)
        all_sprites.add(explosao2)
        
    if len(all_avioes) < 8:
        aviao = Aviao(assets['image_aviao'])
        all_sprites.add(aviao)
        all_avioes.add(aviao)

    print(hits)
    if len(hits):
       lives -= 1

    if lives == 0:
        state = gameover
        pygame.time.delay(500) 
        


    #     ----- Gera saídas
    tela.fill((0,0,0)) 
    tela.blit(assets['background'], (0, i))
    tela.blit(assets['background'], (0, -altura + i))

    if i == altura:
        tela.blit(assets['background'], (0, altura - i))
        i = 0
    i += 5

    # Desenhando na tela
    all_sprites.draw(tela)

    # Desenha score na tela
    text_surface = front_score.render("{:08d}".format(score), True, (255, 100, 200))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura / 2,  10)
    tela.blit(text_surface, text_rect)

    # Desenhando as vidas
    text_surface = front_score.render(chr(9829) * lives, True, (255,0, 0))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (50, 10)
    tela.blit(text_surface, text_rect)


    # ----- Atualiza estado do jogo
    pygame.display.update()                           
    
    score = int(pygame.time.get_ticks()/100)

    if state == gameover:
        while state == gameover:

            tela.fill((0,0,0))  
            tela.blit(assets['tela_fin'], (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                    state = playing

                if event.type == pygame.QUIT:
                     state = over
            pygame.display.update()

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
