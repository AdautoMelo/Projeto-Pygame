#importe e inicialize a biblioteca pygame
import pygame
pygame.init()

# ajuste o tamanho da tela
screen = pygame.display.set_mode((1920, 1080))

#Rode até que o usuario peça para sair

running = True
while running:
    
    #Teste se o usuario clicou no botao de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Prencha o fundo branco da tela com a cor branca
    screen.fill((255,255,255))

    # Desenhe um circulo solido de cor azul no centro da tela

    pygame.draw.circle(screen, (0,0, 255), (250, 250), 75)

    #atualize o display

    pygame.display.flip()

#Pronto! hora de sair

pygame.quit()
