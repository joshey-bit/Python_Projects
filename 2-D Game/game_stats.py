'''create a clss to store game stats'''

class GameStats():
    def __init__(self,alien_settings):
        self.alien_settings = alien_settings
        self.reset_stat()

        # start the game inactive state
        self.game_active = False

        #set high_score
        self.high_score = 0

    def reset_stat(self):
        '''initializing the statiss tht can change during game'''
        self.ship_left = self.alien_settings.number_ship_allowed
        # set the score of the game
        self.score = 0
        # set the level of the game
        self.game_level = 1  # should begin with 1st level