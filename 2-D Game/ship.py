'''
A program to crate ship class
'''
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    '''class to define the ship and its position'''
    def __init__(self,alien_settings,screen):
        '''initialize the ship and its starting position'''
        super().__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        '''load ship image and get its rectangle'''
        self.image = pygame.image.load('images\ship2.bmp').convert()
        self.image.set_colorkey((255, 255, 255))  # to change white background of image to screen background
        self.image = pygame.transform.scale(self.image,(80,50)) # to scale the image to correct pixel size
        self.rect = self.image.get_rect()  #getting rectangle of image
        self.screen_rect = screen.get_rect() #getting rectangle of screen

        '''start each new ship at bottom center of screen'''
        self.rect.centerx = self.screen_rect.centerx #setting ship x-cordinate to center of screen
        self.rect.bottom = self.screen_rect.bottom  #setting ship bottom edge y-coordinate to bottom edge of screen

        '''convert ship rect from integer to float and store it in nevriable'''
        self.center = float(self.rect.centerx)

        '''movement flag'''
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ships movement based on the flag '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_settings.speed_factor #update ships center value not the rect
        if self.moving_left and self.rect.left > 0:
            self.center -= self.alien_settings.speed_factor

        '''update the ship rect centerx as center value'''
        self.rect.centerx = self.center


    def blitme(self):
        '''method to draw ship at specified location (center)'''
        self.screen.blit(self.image,self.rect)

    def ship_center(self):
        '''position the center of ship to screen center'''
        self.center = self.screen_rect.centerx


