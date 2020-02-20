    from Settings import *
    import sys


class TextsObjects:
    def __init__(self):
        self.setting = Settings()
        self.intro_settings = IntroSettings()

        self.display_intro_1 = DisplayText(
            self.intro_settings.intro_text_1,
            self.intro_settings.intro_text_1_pos_x,
            self.intro_settings.intro_text_1_pos_y,
            self.intro_settings.font_size,
            self.setting.light_grey
            )

        self.display_intro_2 = DisplayText(
            self.intro_settings.intro_text_2,
            self.intro_settings.intro_text_2_pos_x,
            self.intro_settings.intro_text_2_pos_y,
            self.intro_settings.font_size,
            self.setting.light_grey
            )

        self.display_intro_title = DisplayText(
            self.intro_settings.intro_text_title,
            self.intro_settings.intro_text_title_pos_x,
            self.intro_settings.intro_text_title_pos_y,
            self.intro_settings.font_size,
            self.setting.light_grey)


class Intro:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.i_setting = IntroSettings()
        self.intro_text = TextsObjects()
        self.clock = pygame.time.Clock()
        self.speed = 50 * setting.time
        self.screen_c_left = setting.screen_width / 2 - self.speed / 2
        self.screen_c_right = setting.screen_width / 2 + self.speed / 2

    def intro_update(self):
        # reset the background so you don't get multiple drawings onscreen
        self.screen.fill(self.setting.dark_blueish)

        if 0 <= self.i_setting.intro_text_1_pos_x <= \
                self.setting.screen_width:

            # Draw the first text
            self.intro_text.display_intro_1.draw_me_with_shadow(
                    self.screen)

        if self.screen_c_left < self.i_setting.intro_text_2_pos_x < \
                self.screen_c_right:

            # Draw the second text
            self.intro_text.display_intro_2.draw_me_with_shadow(
                self.screen)

        pygame.display.update()

    def show_intro(self):
        self.i_setting.intro_text_1_pos_x += self.speed
        # show the intro for self.intro_time amount of time
        for frames in range(0, self.setting.fps * 3):
            # test for events
            for event in pygame.event.get():
                print(event)
                # when the window is closed stop the game loop
                if event.type == pygame.QUIT:
                    sys.exit()

            self.intro_update()
            self.setting.clock.tick(self.setting.fps)
















