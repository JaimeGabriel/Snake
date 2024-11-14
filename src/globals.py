import numpy as np
import pygame

# Program window dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Game window dimensions
GAME_WIDTH = 400
GAME_HEIGHT = 800

# Game window origin coordinates
game_x = (SCREEN_WIDTH - GAME_WIDTH) // 10 
game_y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2 


# Game speed
HZ_GAME = 60
HZ_FPS_RATIO = 4
FPS = HZ_GAME//HZ_FPS_RATIO

# Game size
COLUMNS = 20
ROWS = COLUMNS * GAME_HEIGHT // GAME_WIDTH
CELLSIZE = GAME_WIDTH // COLUMNS


# Colors used in the game
COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 100),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'TRANSPARENT': (0, 0, 0)
}

# ASCII Art
ASCII_ART = """  _____ ____    ____  __  _    ___ 
 / ___/|    \  /    ||  |/ ]  /  _]
(   \_ |  _  ||  o  ||  ' /  /  [_ 
 \__  ||  |  ||     ||    \ |    _]
 /  \ ||  |  ||  _  ||     ||   [_ 
 \    ||  |  ||  |  ||  .  ||     |
  \___||__|__||__|__||__|\_||_____|                                  

"""

