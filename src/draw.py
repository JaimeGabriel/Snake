import pygame
import pandas as pd
import numpy as np

from globals import *
from read import Read

class Draw:

    def __init__(self) -> None:
        self.game_screen_white_border = 5
        self._read = Read()

    def _draw_game_elements(self, snake, fruit) -> None:  
        """
        Draw the game elements, including the game screen border, the fruit and the snake.

        Args:
            snake (list of lists): The coordinates of the snake's cells.
            fruit (list): The coordinates of the fruit.
        """
        # Game screen border
        pygame.draw.rect(surface=screen, 
                         color=COLORS['WHITE'], 
                         rect=(game_x, 
                               game_y, 
                               GAME_WIDTH, 
                               GAME_HEIGHT),
                         width = GAME_FRAME_WIDTH
                        )  
        
        # Fruit
        pygame.draw.rect(surface=screen, 
                            color=COLORS['RED'], 
                            rect=(game_x + fruit[1] * CELLSIZE, 
                                game_y + fruit[0] * CELLSIZE, 
                                CELLSIZE, 
                                CELLSIZE), 
                            width = SNAKE_FRUIT_WIDTH
                            )

        # Snake
        for index, cell in enumerate(snake):
            snake_width = 0 if index == 0 else SNAKE_FRUIT_WIDTH 
            pygame.draw.rect(surface=screen, 
                             color=COLORS['GREEN'], 
                             rect=(game_x + cell[1] * CELLSIZE, 
                                   game_y + cell[0] * CELLSIZE, 
                                   CELLSIZE, 
                                   CELLSIZE), 
                             width = snake_width
                             )
 

    def _draw_score_frame(self) -> None:
        """
        Draw the frame for the live score screen.

        The frame is a white rectangle with a width of 2 pixels.
        """
        pygame.draw.rect(surface=screen, color=COLORS['WHITE'], 
                         rect=(game_x + BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                               game_y, 
                               SCORE_SCREEN_WIDTH, 
                               SCORE_SCREEN_HEIGHT), 
                         width = SCORE_WINDOW_WIDTH)  


    def _draw_live_score(self, score) -> None:
        """
        Draw the live score of the player on the live score screen.

        Args:
            score (int): The current score of the player.
        """
        font = pygame.font.SysFont('Arial', LIVE_SCORE_FONT_SIZE)  
        text_player_score = font.render("Score: " + str(score), True, COLORS['WHITE'])
        screen.blit(source=text_player_score, 
                    dest=[game_x + 2*BLANK_HORIZONTAL_SPACE + GAME_WIDTH,
                          game_y + BLANK_VERTICAL_SPACE])

    def _draw_ascii_art(self) -> None:
            
        """
        Draw the ASCII art on the live score screen.

        """
        font2 = pygame.font.SysFont('Consolas', size=ASCII_ART_FONT_SIZE)  
        lines = ASCII_ART.splitlines()
        for i, line in enumerate(lines):
            text_surface = font2.render(line, True, COLORS['WHITE'])
            screen.blit(text_surface, 
                        (game_x + 2*BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                                       game_y + 2*BLANK_VERTICAL_SPACE + i * PIXELS_LINE_BREAK_ASCII_ART))  
    
    def _draw_top_scores(self, top_scores_list) -> None:
        
        """
        Draw the top 3 scores on the live score screen.

        Args:
            top_scores_list (list of lists): The top scores and the names of the players.
        """
        font_scores = pygame.font.SysFont('Arial', TOP_SCORES_FONT_SIZE)
        header_surface = font_scores.render(f"Top Scores:", True, COLORS['WHITE'])
        screen.blit(header_surface, 
                    (game_x + 2*BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                          game_y + 5*BLANK_VERTICAL_SPACE))

        for i in range(len(top_scores_list)):
            score_surface = font_scores.render(f"{top_scores_list[i][0]}    {top_scores_list[i][1]}", True, COLORS['WHITE'])
            screen.blit(source=score_surface, 
                        dest=(game_x + 2*BLANK_HORIZONTAL_SPACE + GAME_WIDTH,
                              game_y + 6*BLANK_VERTICAL_SPACE + i * PIXELS_LINE_BREAK_TEXT))

    def _draw_pause_menu(self) -> None:
                
        """
        Draw the pause menu on the screen.

        Paint the score frame in red and displays the text "Paused".
        """
        pygame.draw.rect(surface=screen, color=COLORS['RED'], 
                         rect=(game_x + BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                               game_y, 
                               SCORE_SCREEN_WIDTH, 
                               SCORE_SCREEN_HEIGHT), 
                         width = SCORE_WINDOW_WIDTH) 
        
        font = pygame.font.SysFont('Arial', LIVE_SCORE_FONT_SIZE)  
        text_pause = font.render("Paused", True, COLORS['RED'])
        screen.blit(source=text_pause, 
                    dest=[game_x + 7*BLANK_HORIZONTAL_SPACE + GAME_WIDTH,
                          game_y + BLANK_VERTICAL_SPACE])


    def draw_game_over_screen(self) -> None:
        
        """
        Draw the game over screen.

        Paint the score frame in green and displays the text: 
            "Congratulations! You got a top 3 score!. Look at the terminal".
        """
        pygame.draw.rect(surface=screen, color=COLORS['GREEN'], 
                         rect=(game_x + BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                               game_y, 
                               SCORE_SCREEN_WIDTH, 
                               SCORE_SCREEN_HEIGHT), 
                         width = SCORE_WINDOW_WIDTH)  
        
        font = pygame.font.SysFont('Arial', TOP_SCORES_FONT_SIZE)  
        message = ['Congratulations!', 'You got a top 3 score!', 'Look at the terminal']
        for i, line in enumerate(message):
            text_game_over = font.render(line, True, COLORS['GREEN'])
            screen.blit(source=text_game_over, 
                        dest=[game_x + 2*BLANK_HORIZONTAL_SPACE + GAME_WIDTH, 
                              game_y + 8*BLANK_VERTICAL_SPACE + i * PIXELS_LINE_BREAK_TEXT])


    def draw_screen_elements(self, snake_coordinates, fruit_position, pause, score, top_scores_list):
        """"
        Draw all elements on the game screen

        Args:
            snake_coordinates (numpy.ndarray): The coordinates of the snake.
            fruit_position (numpy.ndarray): The coordinates of the fruit.
            pause (bool): Whether the game is paused or not.
            score (int): The current score of the player.
            top_scores_list (list of lists): The top scores and the names of the players.
        """

        screen.fill(color=COLORS['BLACK'])
        self._draw_game_elements(snake_coordinates, fruit_position)
        self._draw_score_frame()
        self._draw_live_score(score)
        self._draw_ascii_art()
        self._draw_top_scores(top_scores_list)
        self.read_top_scores_bool = False
        if pause:
            self._draw_pause_menu()