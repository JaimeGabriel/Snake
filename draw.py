import pygame
from globals import *

class Draw:

    def __init__(self) -> None:
        pass

    def draw_screen(self, snake, fruit) -> None:  
        matrix = np.zeros((ROWS, COLUMNS))
        matrix[fruit[0], fruit[1]] = 2
        matrix[snake[:, 0], snake[:, 1]] = 1
        for row in range(ROWS):
            for col in range(COLUMNS):
                color = COLORS['GREEN'] if matrix[row][col] == 1 else COLORS['RED'] if matrix[row][col] == 2 else COLORS['BLACK']
                pygame.draw.rect(screen, color, (row * CELLSIZE, col * CELLSIZE, CELLSIZE, CELLSIZE))