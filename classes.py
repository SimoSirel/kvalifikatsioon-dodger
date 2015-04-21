__author__ = 'simo.sirel'

import pygame,random

class Ship(pygame.sprite.Sprite):
    """Movable ship with which played dodges obstacles
	Returns: ship object
	Functions: init, reinit, update, moveleft, moveright, stop
	Attributes: speed, location, image"""
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.image = pygame.image.load('icons/ship.png')
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect=self.image.get_rect()
        self.orig_rect_x=round(screen.get_size()[0]/2)
        self.orig_rect_y=round(screen.get_size()[1]*8/10)
        self.speed_num = speed
        self.speed=0
        self.reinit()


    def reinit(self):
        #used to reinitialise ship location after game restarts
        self.rect.x = self.orig_rect_x
        self.rect.y = self.orig_rect_y

    def update(self):
        self.rect.x += self.speed

    def moveleft(self):
        self.speed = -self.speed_num

    def moveright(self):
        self.speed = self.speed_num

    def stop(self):
        self.speed = 0

class obstacle(pygame.sprite.Sprite):
    """Obstacles on the way of the ship
	Returns: obstacle object
	Functions: init, update, rand_data_calc, stop
	Attributes: speed, image, location, scale"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load('icons/asteroid.png')
        self.rand_data_calc()


    def rand_data_calc(self):
        #random based variables for obstacle class
        self.rand_scale = (random.randint(30,100)//10)*10
        self.rand_speed = random.randint(3,6)
        self.rand_loc = random.randint(0,self.screen.get_size()[0])
        self.image = pygame.transform.scale(self.image,(self.rand_scale,self.rand_scale))
        self.rect = self.image.get_rect()
        self.rect.x = self.rand_loc

    def update(self):
        #updates obstacle location and if obstacle gets out of screen reinitializes its variables
        self.rect.y += self.rand_speed
        if self.rect.y >= self.screen.get_size()[1]:
            self.rand_data_calc()