from datetime import date
import pygame
import csv
from draw import Draw
from move import Move
from snake import Snake
from checker import Checker
from fruit import Fruit
from globals import *


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

direction: str

class Game:

    def __init__(self) -> None:
        self._draw = Draw()
        self._move = Move()
        self._snake = Snake()
        self._fruit = Fruit()
        self._checker = Checker(self._snake, self._fruit)
        
        
        
        self.direction = 'RIGHT'
        self.prev_direction = 'RIGHT'
        self.score = 0
        self.player_name = ''
        self.save_score = True
        self.read_top_scores = True
        self.top_scores_list = self._draw.read_top_scores('player_data/top_scores.csv')


        self.best_score = self.top_scores_list[-1][1]
    


    def start(self) -> None:
        run = True
        
        while run:
            clock.tick(FPS)
            pygame.display.set_caption(title="Snake - FPS: {}".format(int(clock.get_fps())))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            # Movimiento del rectángulo basado en las teclas presionadas
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

            

            if self._checker.check_collision_with_self() or self._checker.check_collision_with_wall(self.direction):
                if self.score > self.best_score and input("Save score? (y/n): ").capitalize() == 'Y':
                    self.read_top_scores = True
                    with open('player_data/top_scores.csv', 'a', newline='') as file:
                        if self.player_name == '':
                            self.player_name = input("Enter your name: ")
                        
                        writer = csv.writer(file)
                        writer.writerow([self.player_name, self.score, date.today()])


                self.score = 0
                self._snake.coordinates = np.array([[np.random.randint(0, ROWS - 1), np.random.randint(0, COLUMNS - 1)]])
                self.direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
            
            if self._checker.check_collision_with_fruit():
                self.score += 1
                self._snake.grow()
                self._fruit.respawn(snake=self._snake.coordinates)

            self._snake.move(direction=self.direction, prev_direction=self.prev_direction)

            screen.fill(color=COLORS['BLACK'])

            self._draw.draw_game_screen(self._snake.coordinates, self._fruit.position)
            self._draw.draw_score_frame()
            self._draw.draw_live_score(self.score)
            self._draw.draw_ascii_art()
            if self.read_top_scores:
                self.top_scores_list = self._draw.read_top_scores('player_data/top_scores.csv')
            self._draw.draw_top_scores(self.top_scores_list)
            self.read_top_scores = False
            pygame.display.update()


if __name__ == "__main__":
    Game().start()
    



