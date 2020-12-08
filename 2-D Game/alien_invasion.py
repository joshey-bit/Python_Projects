'''
A program to create alien_invasion game in python using pygame package
'''
import sys
import pygame
from pygame.sprite import Group

'''import settings class'''
from settings import Settings

'''import ship class'''
from ship import Ship

# '''import alien class'''
# from alien import Alien

'''import game functions'''
import game_functions as game_func

'''import game stats'''
from game_stats import GameStats

'''import button'''
from button import Button

'''import scoreboard'''
from scoreboard import ScoreBoard

def run_game():
    '''initialize the game and create screen object'''
    pygame.init()           #initializes the background setting for pygame
    alien_settings = Settings()
    screen = pygame.display.set_mode((alien_settings.screen_width,alien_settings.screen_height)) # creates screen instance of resolution tuple specified
    pygame.display.set_caption('Alien Invasion') # displays the caption 'ALien Invasion' on title bar

    #instance to store game statistics
    stats = GameStats(alien_settings)

    #create instance of a button
    play_button = Button(alien_settings,screen,'Play')

    #create instance of scoreboard
    score_board = ScoreBoard(alien_settings,screen,stats)

    #specify background color
    #background_color = (87,99,240)

    #creating ship instance
    ship = Ship(alien_settings,screen)

    #make group to store the groups of bullets
    bullets = Group()

    #make groups of aliens
    aliens = Group()

    # #make alien instance
    # alien = Alien(alien_settings,screen)

    #create alien fleet
    game_func.create_fleet(alien_settings,screen,aliens,ship)

    #start the main loop for the game
    while True:
        '''watch for keyboard and mouse events'''
        game_func.check_events(alien_settings,screen,ship,bullets,aliens,stats,play_button,score_board)

        #the game can be played only if stats is active
        if stats.game_active:
            '''update the ship position based on keypress'''
            ship.update()

            '''update bullet position and del etra bullets'''
            game_func.update_bullets(alien_settings,screen,ship,aliens,bullets,stats,score_board)

            '''update alien posn after bullet to check colision'''
            game_func.update_aliens(alien_settings,screen,ship,aliens,bullets,stats,score_board)

        '''redraw the screen during each pass, and make the most recently drawn screen visible'''
        game_func.update_screen(alien_settings,screen,ship,bullets,aliens,stats,play_button,score_board)

run_game()



