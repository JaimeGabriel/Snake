import numpy as np
import pygame

SCREEN_WEIGHT = 800
SCREEN_HEIGHT = 800

GAME_WEIGHT = 500
GAME_WEIGHT = 700

FPS = 20

ROWS = 100
COLUMNS = 100

CELLSIZE = SCREEN_HEIGHT // ROWS

screen = pygame.display.set_mode(size=(SCREEN_WEIGHT, SCREEN_HEIGHT))



COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0)
}