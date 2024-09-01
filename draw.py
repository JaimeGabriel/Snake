import pygame
from globals import *

class Draw:

    def __init__(self) -> None:
        pass

    def draw_game_screen(self, snake, fruit) -> None:  
        matrix = np.zeros((ROWS, COLUMNS))
        matrix[fruit[0], fruit[1]] = 2
        matrix[snake[:, 0], snake[:, 1]] = 1

        pygame.draw.rect(screen, COLORS['WHITE'], (game_x - 5, game_y - 5 , GAME_WIDTH + 10 , GAME_HEIGHT + 10))  # 5 píxeles de borde
        #for i in range(5):
        #pygame.draw.rect(screen, COLORS['BLACK'], (game_x, game_y, GAME_WIDTH , GAME_HEIGHT ))  # 5 píxeles de borde
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                color = COLORS['GREEN'] if matrix[row][col] == 1 else COLORS['RED'] if matrix[row][col] == 2 else COLORS['BLACK']
                #pygame.draw.rect(screen, color, (game_x, game_y, GAME_WIDTH , GAME_HEIGHT ))
                pygame.draw.rect(screen, color, (game_x + row * HORIZONTAL_CELLSIZE, game_y + col * VERTICAL_CELLSIZE, HORIZONTAL_CELLSIZE, VERTICAL_CELLSIZE))
                #pygame.draw.rect(screen, color, (game_x + col * HORIZONTAL_CELLSIZE, game_y + row * VERTICAL_CELLSIZE, HORIZONTAL_CELLSIZE, VERTICAL_CELLSIZE))


    def draw_score(self, score) -> None:

        pygame.draw.rect(screen, COLORS['WHITE'], (game_x + 1.1 * COLUMNS * HORIZONTAL_CELLSIZE, game_y - 5, 38 * HORIZONTAL_CELLSIZE, 18 * VERTICAL_CELLSIZE))  # 5 píxeles de borde
        pygame.draw.rect(screen, COLORS['BLACK'], (game_x + 1.11 * COLUMNS * HORIZONTAL_CELLSIZE, game_y, 37 * HORIZONTAL_CELLSIZE, 17 * VERTICAL_CELLSIZE))
        
        font = pygame.font.SysFont('Arial', 24)  # Create a Font object
        text = font.render("Score: " + str(score), True, COLORS['WHITE'])
        screen.blit(text, [game_x + 1.12 * COLUMNS * HORIZONTAL_CELLSIZE, game_y])


        font2 = pygame.font.SysFont('Consolas', 13)  # Fuente más pequeña para el texto ASCII
        # Dividir el arte ASCII en líneas y renderizar cada una por separado
        lines = ascii_art.splitlines()
        for i, line in enumerate(lines):
            text_surface = font2.render(line, True, COLORS['WHITE'])
            screen.blit(text_surface, (game_x + 1.12 * COLUMNS * HORIZONTAL_CELLSIZE, 2*game_y + i * 15))  # 20 es el salto de línea
        
