# # Atualiza a posição da imagem de fundo.
#     background_rect.y -= 1
#     # Se o fundo saiu da janela, faz ele voltar para dentro.
#     # Verifica se o fundo saiu para a esquerda
#     if background_rect.top < 0:
#         background_rect.y += background_rect.height
#         # Verifica se o fundo saiu para a direita
#     if background_rect.bottom >= altura:
#         background_rect.y -= background_rect.height

#     BLACK = (0, 0, 0)
#     tela.fill(BLACK)

#     tela.blit(background, background_rect)
#     # Desenhamos a imagem novamente, mas deslocada em x.
#     background_rect2 = background_rect.copy()
#     if background_rect.top > 0:
#         # Precisamos desenhar o fundo à esquerda
#         background_rect2.x -= background_rect2.height
#     else:
#         # Precisamos desenhar o fundo à direita
#         background_rect2.x += background_rect2.height
#     tela.blit(background, background_rect2)

#     all_sprites.draw(tela)
