'''program to create button class'''

import pygame.font

class Button():
    '''to create button'''
    def __init__(self,alien_settings,screen,msg):
        self.alien_settings = alien_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #creating font attribute
        self.font = pygame.font.SysFont(None,self.alien_settings.text_size)

        #creating button rect
        self.rect = pygame.Rect(0,0, self.alien_settings.button_width, self.alien_settings.button_height)
        self.rect.center = self.screen_rect.center

        #button message has to prepared once.
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''method to turn message into image and position it center of button'''
        self.msg_image = self.font.render(msg,True, self.alien_settings.text_color, self.alien_settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''method to draw blank button and messge over it'''
        self.screen.fill(self.alien_settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)