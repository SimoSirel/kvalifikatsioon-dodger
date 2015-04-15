import pygame
pygame.init()
running=True

size=width,height=320,700
screen = pygame.display.set_mode(size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    pygame.display.flip()
pygame.quit()