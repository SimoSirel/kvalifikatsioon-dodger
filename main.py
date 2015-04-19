__author__ = 'simo.sirel'

import pygame,classes
pygame.init()
running=True

size=width,height=700,500
screen = pygame.display.set_mode(size)

ship=classes.Ship(5,[250,400])
ships=pygame.sprite.Group(ship)
asteroid=classes.obstacle()
debris=pygame.sprite.Group(asteroid)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: ship.moveleft()
            if event.key == pygame.K_RIGHT: ship.moveright()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                ship.stop()

    screen.fill([255,255,255])
    ships.draw(screen)
    debris.draw(screen)
    ships.update()
    debris.update()
    pygame.time.Clock().tick(60)
    pygame.display.flip()
pygame.quit()