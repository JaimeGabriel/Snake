import pygame
import pandas as pd
from globals import *
from read import Read

class Draw:

    def __init__(self) -> None:
        self.game_screen_white_border = 5
        self._read = Read()

    def draw_game_screen(self, snake, fruit) -> None:  
        matrix = np.zeros((ROWS, COLUMNS))
        matrix[fruit[0], fruit[1]] = 2
        matrix[snake[:, 0], snake[:, 1]] = 1

        pygame.draw.rect(screen, COLORS['WHITE'], (game_x - self.game_screen_white_border, game_y - self.game_screen_white_border , GAME_WIDTH + 2 * self.game_screen_white_border , GAME_HEIGHT + 2 * self.game_screen_white_border))  # Para el marco
 
        for row in range(ROWS):
            for col in range(COLUMNS):
                color = COLORS['GREEN'] if matrix[row][col] == 1 else COLORS['RED'] if matrix[row][col] == 2 else COLORS['BLACK']
                pygame.draw.rect(screen, color, (game_x + col * CELLSIZE, game_y + row * CELLSIZE, CELLSIZE, CELLSIZE), width = 2 if color==COLORS['GREEN'] else 0)


    # def draw_live_score(self, score, filename_top_scores, read_top_scores) -> None:

    #     self._draw_score_frame()
    #     self._draw_live_score(score)
    #     self._draw_ascii_art()
    #     if read_top_scores:
    #         top_scores_list = self._read_top_scores(filename_top_scores)
    #         print("read")
    #     self._draw_top_scores(filename_top_scores, top_scores_list)
        

    def draw_score_frame(self) -> None:

        pygame.draw.rect(surface=screen, color=COLORS['WHITE'], 
                         rect=(game_x + 1.1  * COLUMNS * CELLSIZE, 
                               game_y - 5, 
                               GAME_WIDTH * 0.85, 
                               GAME_HEIGHT // 2 + 2 * self.game_screen_white_border), 
                         width = 2)  
        #pygame.draw.rect(screen, COLORS['BLACK'], (game_x + 1.11 * COLUMNS * CELLSIZE, game_y, GAME_WIDTH, GAME_HEIGHT // 2))


    def draw_live_score(self, score) -> None:

        font = pygame.font.SysFont('Arial', 24)  
        text_player_score = font.render("Score: " + str(score), True, COLORS['WHITE'])
        screen.blit(text_player_score, [game_x + 1.12 * COLUMNS * CELLSIZE, game_y*1.1])

    def draw_ascii_art(self) -> None:

        font2 = pygame.font.SysFont('Consolas', 13)  
        lines = ASCII_ART.splitlines()
        for i, line in enumerate(lines):
            text_surface = font2.render(line, True, COLORS['WHITE'])
            screen.blit(text_surface, (game_x + 1.12 * COLUMNS * CELLSIZE, 2*game_y + i * 15))  

    def read_top_scores(self, filename_top_scores) -> tuple[list, list]:
        
        top_scores_dataframe = pd.read_csv(filename_top_scores).sort_values(by='score', ascending=False).head(3)
        print("read")
        return top_scores_dataframe.values.tolist()
    
    def draw_top_scores(self, top_scores_list) -> None:

        font_scores = pygame.font.SysFont('Arial', 18)

        top_scores_header = top_scores_list[0]
        header_surface = font_scores.render(f"Top Scores:", True, COLORS['WHITE'])
        screen.blit(header_surface, (game_x + 1.12 * COLUMNS * CELLSIZE, game_y + 200))


        for i in range(len(top_scores_list)):
            score_surface = font_scores.render(f"{top_scores_list[i][0]}    {top_scores_list[i][1]}", True, COLORS['WHITE'])
            screen.blit(score_surface, (game_x + 1.12 * COLUMNS * CELLSIZE, game_y + 200 + 20*(i+1)))

        # for i, row in enumerate(top_scores_list.splitlines()):
        #     row_surface = font_scores.render(f"{row[0]}    {row[1]}     {row[2]}", True, COLORS['WHITE'])
        #     screen.blit(row_surface, (game_x + 1.12 * COLUMNS * CELLSIZE, game_y + 200 + i * 20))

    def draw_new_best_score_screen(self) -> None:

        font = pygame.font.SysFont('Arial', 24)  
        text_player_score = font.render("New Best Score!", True, COLORS['WHITE'])
        screen.blit(text_player_score, [game_x + 1.12 * COLUMNS * CELLSIZE, game_y])

    def pause_menu(self) -> None:

                             
        pygame.draw.rect(surface=screen, 
                         color=COLORS['RED'], 
                         rect=(game_x + 1.1  * COLUMNS * CELLSIZE, 
                               game_y - 5, 
                               GAME_WIDTH * 0.85, 
                               GAME_HEIGHT // 2 + 2 * self.game_screen_white_border), 
                         width = 2)  

        
        
        font = pygame.font.SysFont('Arial', 24)  
        text_pause = font.render("Paused", True, COLORS['RED'])
        screen.blit(text_pause, [game_x + 1.12 * COLUMNS * CELLSIZE, game_y + 200 + 20*(5+1)])


    def draw_game_over_screen(self) -> None:

        pygame.draw.rect(surface=screen, color=COLORS['GREEN'], 
                         rect=(game_x + 1.1  * COLUMNS * CELLSIZE, 
                               game_y - 5, 
                               GAME_WIDTH * 0.85, 
                               GAME_HEIGHT // 2 + 2 * self.game_screen_white_border), 
                         width = 2)  
        
        font = pygame.font.SysFont('Arial', 24)  
        message = ['Congratulations!', 'You got a top 3 score!', 'Look at the terminal']
        for i, line in enumerate(message):
            text_game_over = font.render(line, True, COLORS['GREEN'])
            screen.blit(text_game_over, [game_x + 1.12 * COLUMNS * CELLSIZE, game_y + 150 + 30*(5+i)])


    def draw_screen_elements(self, snake_coordinates, fruit_position, score):
        """"Draw all elements on the game screen"""

        screen.fill(color=COLORS['BLACK'])
        self.draw_game_screen(snake_coordinates, fruit_position)
        self.draw_score_frame()
        self.draw_live_score(score)
        self.draw_ascii_art()
        if self.read_top_scores:
            self.top_scores_list = self._read.read_top_scores('player_data/top_scores.csv')
        self.draw_top_scores(self.top_scores_list)
        self.read_top_scores_bool = False
        