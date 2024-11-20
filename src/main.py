from datetime import date
import pygame
import csv
import numpy as np

from draw import Draw
from snake import Snake
from checker import Checker
from fruit import Fruit
from globals import *
from read import Read



pygame.init()
clock = pygame.time.Clock()


direction: str

class Game:

    def __init__(self) -> None:
        self._draw = Draw()
        self._snake = Snake()
        self._fruit = Fruit()
        self._read = Read()
        self._checker = Checker(self._snake, self._fruit)
        
        self.pause = False
        self.frame_counter = 0
        self.direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.prev_direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.score = 0
        self.player_name = ''
        self.top_scores_list = self._read.read_top_scores('player_data/top_scores.csv')
        self.best_score = self.top_scores_list[-1][1]
    

    def reset_game_state(self) -> None:
        """
        Reset score, snake coordinates and snake direction
        """
        self.score = 0
        self._snake.coordinates = np.array([[np.random.randint(0, ROWS - 1), \
                                                    np.random.randint(0, COLUMNS - 1)]])
        self.direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.prev_direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])


    def start(self) -> None:
        run = True
        
        while run:
            # We use the frame counter to get higher inputs per second from the user without having to use higher FPS
            self.frame_counter += 1
            if self.frame_counter > 1000:
                self.frame_counter = 0

            # Window title
            clock.tick(HZ_GAME)
            title = f'Snake. Hz: {int(clock.get_fps())}/{HZ_GAME}. \
                FPS: {int(clock.get_fps()/HZ_FPS_RATIO)}/{FPS}'
            pygame.display.set_caption(title=title)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the x button is pressed, end the game
                    run = False

                elif event.type == pygame.KEYUP:
                    # If space is pressed, toggle the pause state
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause

            keys = pygame.key.get_pressed()

            if not self.pause:
                

                # Movement of the snake
                if keys[pygame.K_RIGHT] and self.direction != 'LEFT':
                    self.prev_direction = self.direction
                    self.direction = 'RIGHT'

                if keys[pygame.K_LEFT]and self.direction != 'RIGHT':
                    self.prev_direction = self.direction
                    self.direction = 'LEFT'

                if keys[pygame.K_UP] and self.direction != 'DOWN':
                    self.prev_direction = self.direction
                    self.direction = 'UP'

                if keys[pygame.K_DOWN] and self.direction != 'UP':
                    self.prev_direction = self.direction
                    self.direction = 'DOWN'    


                # Check for collisions and move the snake. This is only made 1/HZ_FPS_RATIO os the total updates
                if self.frame_counter % HZ_FPS_RATIO == 0:
                    # Check for collision with self or wall
                    if self._checker.check_collision(self.direction):
                        # Draw 'game over' screen if a new top 3 score is achieved
                        if self.score > self.best_score:
                            self._draw.draw_game_over_screen()
                            pygame.display.update()
                            # Ask to save the score
                            if input("Save score? (y/n): ").capitalize() == 'Y':
                                with open('player_data/top_scores.csv', 'a', newline='') as file:
                                    if self.player_name == '':
                                        self.player_name = input("Enter your name: ")
                                    
                                    writer = csv.writer(file)
                                    writer.writerow([self.player_name, self.score, date.today()])
                                self.top_scores_list = self._read.read_top_scores('player_data/top_scores.csv')
                                    

                        # Reset game state
                        self.reset_game_state()
                    
                    # Check for collision with fruit
                    if self._checker.check_collision_with_fruit():
                        self.score += 1
                        self._snake.grow()
                        self._fruit.respawn(snake=self._snake.coordinates)

                    self._snake.move(direction=self.direction, prev_direction=self.prev_direction)

                    # Draw and update the game screen
                    self._draw.draw_screen_elements(self._snake.coordinates,
                                                    self._fruit.position, 
                                                    self.pause,
                                                    self.score,
                                                    self.top_scores_list)
                    pygame.display.update()

            elif self.pause == True:                

                # Draw and update the game screen
                self._draw.draw_screen_elements(self._snake.coordinates,
                                                self._fruit.position, 
                                                self.pause,
                                                self.score,
                                                self.top_scores_list)
                pygame.display.update()


if __name__ == "__main__":
    Game().start()
    



