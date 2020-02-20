import pygame
from Menu import *


class Player:
    def __init__(self, screen, setting):
        self.setting = setting
        self.screen = screen
        self.intro_text = TextsObjects()

        # player settings
        # player size
        self.player_width = 60
        self.player_height = 48

        # load the player image
        self.player = pygame.image.load("../Images/player.bmp")

        self.player_position_x = \
            setting.screen_width / 2 - self.player_width / 2

        self.player_position_y = \
            setting.screen_height / 2 - self.player_height / 2

        # player speed
        self.player_speed_left = 0
        self.player_speed_right = 0
        self.player_speed_up = 0
        self.player_speed_down = 0

        # player speeding up
        self.player_acceleration = 450
        self.player_acceleration_left = \
            -1 * self.player_acceleration * setting.time
        self.player_acceleration_right = \
            self.player_acceleration * setting.time
        self.player_acceleration_up = \
            -1 * self.player_acceleration * setting.time
        self.player_acceleration_down = \
            self.player_acceleration * setting.time

    def update(self):
        # left boundary
        if self.player_position_x <= 0:
            self.player_speed_left = 0
        # right boundary
        elif self.player_position_x >= self.setting.screen_width - \
                self.player_width:
            self.player_speed_right = 0
        # upper boundary
        if self.player_position_y <= 0:
            self.player_speed_up = 0
        # bottom boundary
        elif self.player_position_y >= self.setting.screen_height - \
                self.player_height:
            self.player_speed_down = 0
        # make the player move
        self.player_position_x += \
            self.player_speed_right + self.player_speed_left
        self.player_position_y += \
            self.player_speed_up + self.player_speed_down

    # draw the player on the screen
    def draw_me(self):
        # draw the player on the screen
        self.screen.blit(self.player, (self.player_position_x,
                                       self.player_position_y))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, setting, player):
        super().__init__()
        self.screen = screen

        self.bullet_width = 3
        self.bullet_height = 5

        self.bullet_x = player.player_position_x + player.player_width / 2
        self.bullet_y = player.player_position_y + self.bullet_height

        self.color = setting.white
        self.speed_factor = -400 * setting.time

        # keep track of the bullets to remove them
        self.bullet_list = []

    def update(self, bullets):
        for bullet in bullets:
            self.bullet_list.append(bullet)

        if self.bullet_y <= 0 - self.bullet_height:
            bullets.remove(self.bullet_list[0])
            self.bullet_list.pop(0)
        else:
            self.bullet_y += self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, [self.bullet_x,
                                                   self.bullet_y,
                                                   self.bullet_width,
                                                   self.bullet_height])
