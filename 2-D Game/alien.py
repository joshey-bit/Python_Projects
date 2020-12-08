'''
A program to create alien class
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to create an alien and draw it on the screen'''
    def __init__(self,alien_settings,screen):
        super().__init__()
        self.alien_settings = alien_settings
        self.screen = screen

        #load the alien image and get the resctangle
        self.image = pygame.image.load(r'images/alien.bmp').convert()
        self.image.set_colorkey((255,255,255)) #to match image background with screen background
        self.img = pygame.transform.scale(self.image,(40,35))
        self.rect = self.img.get_rect() #to get the rectangle of image


        #position the alien to top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #set the float value of alien postion
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''method to update the x posistion of alien'''
        self.x += (self.alien_settings.alien_speed_factor * self.alien_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        '''method to add alien on screen'''
        self.screen.blit(self.img, self.rect)

    def check_edges(self):
        '''method to check whether the alien reaches edges'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
