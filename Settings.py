import pygame

pygame.init()


class Settings:
    def __init__(self):

        # screen size
        self.screen_width = 800
        self.screen_height = 500

        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.dark_red = (150, 0, 0)
        self.dark_green = (0, 150, 0)
        self.dark_blue = (0, 0, 150)
        self.light_grey = (200, 200, 200)
        self.dark_blueish = (50, 50, 100)

        # set clock and fps
        self.clock = pygame.time.Clock()
        self.fps = 60
        # calculate the seconds in every frame
        self.time = 1 / self.fps

        # bullet limit
        self.bullet_limit = 2


class IntroSettings:
    def __init__(self):
        self.setting = Settings()
        self.font_size = 100
        self.timer_font_size = 10

        self.intro_text_1_pos_x = (self.setting.screen_width / 2) - 100
        self.intro_text_1_pos_y = \
            (self.setting.screen_height / 2 - self.font_size)
        self.intro_text_1 = "A game by:"

        self.intro_text_2_pos_x = (self.setting.screen_width / 2)
        self.intro_text_2_pos_y = \
            (self.setting.screen_height / 2 + self.font_size)
        self.intro_text_2 = "Mark Olieman"

        self.intro_text_title_pos_x = (self.setting.screen_width / 2)
        self.intro_text_title_pos_y = (self.setting.screen_height + self.font_size)
        self.intro_text_title = "Alien Invasion!"

        self.intro_text_timer_pos_x = 20
        self.intro_text_timer_pos_y = 20

        self.speed = -2


class DisplayText:
    def __init__(self, text, pos_x, pos_y, font_size, text_color):

        self.font = pygame.font.Font("freesansbold.ttf", font_size)

        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (pos_x, pos_y)

        self.shadow_color = (0, 0, 0)

        self.text_surf_shadow = self.font.render(text, True, self.shadow_color)
        self.text_rect_shadow = self.text_surf.get_rect()
        self.text_rect_shadow.center = (pos_x + 10, pos_y + 5)

    def draw_me(self, screen):
        screen.blit(self.text_surf, self.text_rect)

    def draw_me_with_shadow(self, screen):
        screen.blit(self.text_surf_shadow, self.text_rect_shadow)
        screen.blit(self.text_surf, self.text_rect)



