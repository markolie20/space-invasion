import pygame
import sys
from Entities import *
from Settings import *
from Menu import *


def events(bullets, player, screen, setting):
    # test for events
    for event in pygame.event.get():
        # when the window is closed stop the game loop
        if event.type == pygame.QUIT:
            sys.exit()

        # look if a key is pressed
        if event.type == pygame.KEYDOWN:

            # change the speed to the right
            # if the right arrow key is pressed
            if event.key == pygame.K_RIGHT:
                player.player_speed_left = 0
                player.player_speed_right = player.player_acceleration_right

            # change the speed to the left
            # if the left arrow key is pressed
            elif event.key == pygame.K_LEFT:
                player.player_speed_right = 0
                player.player_speed_left = player.player_acceleration_left

            # change the speed upwards
            # if the up arrow key is pressed
            elif event.key == pygame.K_UP:
                player.player_speed_down = 0
                player.player_speed_up = player.player_acceleration_up

            # if the down arrow key is pressed
            elif event.key == pygame.K_DOWN:
                player.player_speed_up = 0
                player.player_speed_down = player.player_acceleration_down

            elif event.key == pygame.K_SPACE:
                # give the bullet speed so it moves
                # bullet.bullet_speed = bullet.bullet_acceleration
                if len(bullets) > setting.bullet_limit:
                    pass
                else:
                    new_bullet = Bullet(screen, setting, player)
                    bullets.add(new_bullet)

        # when the keys are released stop the action
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.player_speed_right = 0
            elif event.key == pygame.K_LEFT:
                player.player_speed_left = 0
            elif event.key == pygame.K_UP:
                player.player_speed_up = 0
            elif event.key == pygame.K_DOWN:
                player.player_speed_down = 0


intro_text = TextsObjects()


def update(player, setting, bullets, screen):
    screen.fill(setting.black)

    player.update()
    player.draw_me()

    bullets.update(bullets)

    for bullet in bullets:
        bullet.draw_bullet()
