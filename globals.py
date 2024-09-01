import numpy as np
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GAME_WIDTH = 400
GAME_HEIGHT = 700

AR = GAME_HEIGHT / GAME_WIDTH

FPS = 20

COLUMNS = 50 
ROWS = 50

CELLSIZE = int(GAME_WIDTH / COLUMNS)
HORIZONTAL_CELLSIZE = CELLSIZE
VERTICAL_CELLSIZE = int(CELLSIZE * AR)




screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))


game_x = (SCREEN_WIDTH - GAME_WIDTH) // 10
game_y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2



COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'TRANSPARENT': (0, 0, 0)
}

ascii_art = """  _____ ____    ____  __  _    ___ 
 / ___/|    \  /    ||  |/ ]  /  _]
(   \_ |  _  ||  o  ||  ' /  /  [_ 
 \__  ||  |  ||     ||    \ |    _]
 /  \ ||  |  ||  _  ||     ||   [_ 
 \    ||  |  ||  |  ||  .  ||     |
  \___||__|__||__|__||__|\_||_____|                                  

"""