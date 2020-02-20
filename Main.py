import pygame
from Settings import *
from Entities import *
from Game_functions import *
from Menu import *

# make the modules available
setting = Settings()

screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
pygame.display.set_caption("Alien Invasion, By Mark Olieman")

intro = Intro(screen, setting)
player = Player(screen, setting)
bullet = Bullet(screen, setting, player)
intro_set = IntroSettings()

# initizialize pygame
pygame.init()
pygame.mixer.init()

# initizialize the screen and set a caption


# function to start gaming
def gaming():
    bullets = pygame.sprite.Group()
    intro.show_intro()
    intro_set.intro_text_1_pos_x += intro.speed
    print(intro_set.intro_text_1_pos_x)
    # Game Loop
    while True:
        # check events and make actions happen
        events(bullets, player, screen, setting)

        # update everything and draw bullets
        update(player, setting, bullets, screen)

        # update screen at certain fps
        pygame.display.update()
        setting.clock.tick(setting.fps)


# Start the game
gaming()

# Stop the game
pygame.quit()
