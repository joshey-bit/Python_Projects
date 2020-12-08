'''a program to create a score board'''
import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    def __init__(self,alien_Settings,screen,stats):
        self.alien_settings = alien_Settings
        self.stats = stats
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #create font color and font instatance
        self.font_color = (30,30,30)
        self.font = pygame.font.SysFont(None,40)

        #prepare the image of score_font
        self.prep_score()
        #prepare the image of highscore
        self.prep_highscore()
        #prepare the image of level
        self.prep_level()
        #prepare image of ships left
        self.prep_ships()

    def prep_score(self):
        self.rounded_score = int(round(self.stats.score,-1)) #round of the score to neares 10s 100s etc andconvert the score into string
        self.score = f'{self.rounded_score:,}'
        #render the text into image
        self.score_image = self.font.render(self.score, True, self.font_color, self.alien_settings.background_color)

        #create score rect and position it to top right of screen
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_highscore(self):
        self.rounded_highscore = int(round(self.stats.high_score,-1))
        self.highscore = f'{self.rounded_highscore:,}'

        #render the text to image
        self.highscore_image = self.font.render(self.highscore,True,self.font_color, self.alien_settings.background_color)

        # create highscore rect and position it to top center of screen
        self.highscore_image_rect = self.highscore_image.get_rect()
        self.highscore_image_rect.center = self.screen_rect.center
        self.highscore_image_rect.top = self.score_image_rect.top

    def prep_level(self):
        '''method to create level image under the score image'''
        self.level_image = self.font.render(str(self.stats.game_level),True,self.font_color, self.alien_settings.background_color)

        # create level image rect and position it to top right of screen below score image
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10

    def prep_ships(self):
        #create group of ships on the top left of screen
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.alien_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def draw_score(self):
        #draw score image
        self.screen.blit(self.score_image,self.score_image_rect)
        #draw highscore image
        self.screen.blit(self.highscore_image,self.highscore_image_rect)
        #draw level image
        self.screen.blit(self.level_image,self.level_rect)
        #draw ships left on screen
        self.ships.draw(self.screen)


