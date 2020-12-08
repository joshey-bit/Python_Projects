'''
A program to store the functions/actions involved in game
'''
import sys

import pygame

from bullets import Bullet

from alien import Alien

from time import sleep

from random import randint

def check_keydown_events(event,alien_settings,screen,ship,bullets,aliens,stats,score_board):
    '''respond to keypress'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets,alien_settings,screen,ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        if event.key and not stats.game_active:  # the action of button click is only considered if game active is False
            play_game(stats, aliens, bullets, alien_settings, screen, ship,score_board)

def check_keyup_events(event,ship):
    '''respond to key release'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(alien_settings,screen,ship,bullets,aliens,stats,play_button,score_board):
    '''fuction to watch for keyboard and mouse events'''
    for event in pygame.event.get(): #event is an action performed by the user, and forloop(eventloop)
        if event.type == pygame.QUIT: #event loop performs task based on event, like exiting the pygame window
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,alien_settings,screen,ship,bullets,aliens,stats,score_board) #calling above function
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,alien_settings,screen,ship,score_board)


def update_screen(alien_settings,screen,ship,bullets,aliens,stats,play_button,score_board):
    '''function to update the image on screen and flip to new screen'''
    screen.fill(alien_settings.background_color)
    '''redraw bullets before the ship, to keep the old bullet positions'''
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    '''redraw ship image'''
    ship.blitme()

    '''redraw alien image'''
    # aliens.draw(screen)
    for alien in aliens.sprites():
        alien.blitme()

    #to print the score
    score_board.draw_score()

    # to display the button
    if not stats.game_active:
        play_button.draw_button()

    '''make the most recently drawn screen visible'''
    pygame.display.flip()

def update_bullets(alien_settings,screen,ship,aliens,bullets,stats,score_board):
    '''function to update bullet position and del etra bullets'''
    #update bullet position
    bullets.update()

    #deleting bullets when they cross the screen top
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(alien_settings,screen,ship,aliens,bullets,stats,score_board)



def check_bullet_alien_collision(alien_settings,screen,ship,aliens,bullets,stats,score_board):
    # check for bullet and alien collision
    # if collided remove alien and bullet tht collided
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collision:
        #code to update score for all aliens hit
        for aliens in collision.values():
            stats.score += alien_settings.alien_point * len(aliens)
            score_board.prep_score()
        check_highscore(stats,score_board)

    if len(aliens) == 0:
        # empty the existing bullets, speed up the game, increase the level and create a new fleet
        bullets.empty()
        alien_settings.increase_speed()
        #increase the level
        stats.game_level += 1
        score_board.prep_level()

        create_fleet(alien_settings, screen, aliens, ship)


def update_aliens(alien_settings,screen,ship,aliens,bullets,stats,score_board):
    '''function to update alien position'''
    check_fleet_edges(alien_settings,aliens)
    aliens.update()
    # for alien in aliens.sprites():
    #     alien.update()

    #check for alien ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,alien_settings,screen,ship,score_board)

    #checck if alien reached bottom
    check_aliens_bottom(alien_settings, screen, aliens, bullets, ship, stats,score_board)

def ship_hit(stats,aliens,bullets,alien_settings,screen,ship,score_board):
    '''function to respond if ship is hit by alien'''
    if stats.ship_left > 0:
        #update the stats, by subtracting number of ship left
        stats.ship_left -= 1

        #update the number of ships left on score board
        score_board.prep_ships()

        #empty the bullets and aliens
        aliens.empty()
        bullets.empty()

        #create new fleet and position ship to center
        create_fleet(alien_settings,screen,aliens,ship)
        ship.ship_center()

        #pause the game
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def fire_bullets(bullets,alien_settings,screen,ship):
    '''function to fire restricted amount of bullets when space is pressed'''
    if len(bullets) < alien_settings.bullets_allowed:
        new_bullet = Bullet(alien_settings,screen,ship)
        bullets.add(new_bullet)

def create_fleet(alien_settings,screen,aliens,ship):
    '''functiom to create aliens in a row'''
    #create an alien and find number of aliens in a row
    #space between two aliens is 1 alien width
    alien = Alien(alien_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_of_aliens = get_aliennumber_x(alien_settings,alien_width)
    number_of_rows = get_number_rows(alien_settings,alien_height,ship)

    for row_number in range(number_of_rows):
        #create frst row of aliens
        for alien_number in range(number_of_aliens):
            create_alien(alien_settings,screen,alien_width,alien_height,alien_number,row_number,aliens)


def get_aliennumber_x(alien_settings,alien_width):
    available_space_x = alien_settings.screen_width - \
                        (2 * alien_width)  # space avalaible is betwwen two extreme margins
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def get_number_rows(alien_settings,alien_height,ship):
    available_space_y = alien_settings.screen_height - \
                        (6 * alien_height) - ship.rect.height
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows

def create_alien(alien_settings,screen,alien_width,alien_height,alien_number,row_number,aliens):
    # create an alien and add it to aliens group
    alien = Alien(alien_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def check_fleet_edges(alien_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(alien_settings,aliens)
            break


def change_direction(alien_settings,aliens):
    '''fuction to drop the alien fleet and change the direction of alien fleet'''
    for alien in aliens.sprites():
        alien.rect.y += alien_settings.down_speed
    alien_settings.fleet_direction *= -1

def check_aliens_bottom(alien_settings,screen,aliens,bullets,ship,stats,score_board):
    #check wheter the alien crossed the screen bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,aliens,bullets,alien_settings,screen,ship,score_board)
            break

def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,alien_settings,screen,ship,score_board):
    '''fucntion to enact play_button click'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) #if mouse x,y cordinate overlap button rect, its button clicl
    if button_clicked and not stats.game_active: #the action of button click is only considered if game active is False
        play_game(stats,aliens,bullets,alien_settings,screen,ship,score_board)

def play_game(stats,aliens,bullets,alien_settings,screen,ship,score_board):
    '''function to start/reset game after play button is clicked'''
    #reset the dynamic settings of game
    alien_settings.initialize_dynamic_settings()

    #hide mouse cursor
    pygame.mouse.set_visible(False)

    #reset the game stats and set game_active to true
    stats.reset_stat()
    stats.game_active = True

    #reset the scoreboard
    score_board.prep_score()
    score_board.prep_highscore()
    score_board.prep_level()
    score_board.prep_ships()

    # empty the bullets and aliens
    aliens.empty()
    bullets.empty()

    # create new fleet and position ship to center
    create_fleet(alien_settings, screen, aliens, ship)
    ship.ship_center()

def check_highscore(stats,score_board):
    '''function to check high score and update it'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_highscore()













