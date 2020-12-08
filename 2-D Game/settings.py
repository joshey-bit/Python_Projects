'''
program to create a settings class for alien_invasion.py
'''
class Settings():
    '''class to set the default attributes'''
    def __init__(self):
        '''static settings'''
        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (87,99,240)

        #ship settings
        self.number_ship_allowed = 3

        # bullet settings
        self.bullet_width = 4
        self.bullet_height = 10

        self.bullet_color = (0,0,0) # setting bullet color to black
        self.bullets_allowed= 3

        #alien_speed_setting
        self.down_speed = 5 #static property


        #button settings
        self.button_width = 150
        self.button_height = 50
        self.button_color = (0,255,0) #green color

        #text settings
        self.text_size = 40
        self.text_color = (255,255,255) #white color

        '''dynamic settings'''
        self.initialize_dynamic_settings()

        '''speed up scale'''
        self.speed_up_scale = 1.1

        '''score up scale'''
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        '''method to det the dynamic setting attributes'''
        # ship speed factor
        self.speed_factor = 1
        #bullet speed factor
        self.bullet_speed_factor = 2
        #alien speed factor
        self.alien_speed_factor = 0.3
        # for right direction +1, for left direction -1
        self.fleet_direction = 1

        #set alien hit score point
        self.alien_point = 50

    def increase_speed(self):
        '''method to inrease the speed of whole game and increase score points'''
        self.speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

        self.alien_point = int(self.alien_point * self.score_scale)
