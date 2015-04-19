__author__ = 'simo.sirel'

import pygame,random

class Ship(pygame.sprite.Sprite):
    """Movable ship with which one dodges obstacles
	Returns: ship object
	Functions: reinit, update, moveleft, moveright, stop
	Attributes: speed, loc"""
    def __init__(self,speed,loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('icons/ship.png')
        self.image = pygame.transform.scale(self.image,(64,64))
        screen = pygame.display.get_surface()
        self.rect=self.image.get_rect()
        self.orig_rect_x=loc[0]             #tahaks kasutada width, aga see lõhub failid ära
        self.orig_rect_y=loc[1]             #tahaks kasutada width, aga see lõhub failid ära
        self.speed_num = speed
        self.speed=0
        self.reinit()


    def reinit(self):
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
	Functions: reinit, update, moveleft, moveright
	Attributes: speed"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('icons/asteroid.png')
        self.rand_data_calc()
        self.image = pygame.transform.scale(self.image,(self.rand_scale,self.rand_scale))
        self.rect = self.image.get_rect()
        self.rect.x = self.rand_loc


    def rand_data_calc(self):
        self.rand_scale = (random.randint(30,100)//10)*10
        self.rand_speed = random.randint(3,6)
        self.rand_loc = random.randint(0,700)      #tahaks kasutada width, aga see lõhub failid ära

    def update(self):
        self.rect.y += self.rand_speed

