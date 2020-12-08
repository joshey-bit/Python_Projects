'''
program to create bullets class
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''a class tht stores attributes of bullet'''
    def __init__(self,alien_settings,screen,ship):
        '''create bullet objetc at ships current position'''
        super().__init__()
        self.screen = screen

        #creating bullet rect at (0,0) and place it to ccorrect position
        self.rect = pygame.Rect(0,0,alien_settings.bullet_width,alien_settings.bullet_height) #to create the bullet rectangle
        # setting bullet position to ship position
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top  #bullet should emerge from the top of ship

        #bullet position as decimal
        self.y_position = float(self.rect.y)

        self.color = alien_settings.bullet_color
        self.speed_factor = alien_settings.bullet_speed_factor

    def update(self):
        '''method to move bullet upwards'''
        self.y_position -= self.speed_factor

        #update bullet rect position
        self.rect.y = self.y_position

    def draw_bullet(self):
        '''method to draw bullet on screen'''
        pygame.draw.rect(self.screen, self.color,self.rect)

