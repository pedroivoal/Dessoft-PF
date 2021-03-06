def load_assets():
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

    # tela de vitória
    assets['tela_fin2'] = pygame.image.load(r'img\screen_final1.png').convert()
    assets['tela_fin2']= pygame.transform.scale(assets['tela_fin2'],(largura,altura))

    # imagem do ufo
    assets['image_aviao'] = pygame.image.load(r'img\ufo2.png').convert_alpha()
    assets['image_aviao'] = pygame.transform.scale(assets['image_aviao'],(largura_aviao,altura_aviao))

    # imagem da nave 1 do jogador
    assets['image_nave'] = pygame.image.load(r'img\ITS1.png').convert_alpha()
    assets['image_nave'] = pygame.transform.scale(assets['image_nave'],(largura_nave,altura_nave))
    
    # imagem da nave 2 do jogador
    assets['image_nave2'] = pygame.image.load(r'img\ITS2.png').convert_alpha()
    assets['image_nave2'] = pygame.transform.scale(assets['image_nave2'],(largura_nave,altura_nave2))

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
 
    # carrega os sons do jogo 
    pygame.mixer.music.load(r'som\music.mp3')
    pygame.mixer.music.load(r'som\musicgame.mp3')
    pygame.mixer.music.load(r'som\endmusic.mp3')
    pygame.mixer.music.set_volume(0.2)
    assets['explosao'] = pygame.mixer.Sound(r'som\explosao.mp3')
    
    return assets

