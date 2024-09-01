import pygame
from draw import Draw
from move import Move
from snake import Snake
from checker import Checker
from fruit import Fruit
from globals import *


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size=(SCREEN_WEIGHT, SCREEN_HEIGHT))

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
                print(self.direction, self.prev_direction)

            if keys[pygame.K_LEFT]and self.direction != 'RIGHT':
                self.prev_direction = self.direction
                self.direction = 'LEFT'
                print(self.direction, self.prev_direction)

            if keys[pygame.K_UP] and self.direction != 'DOWN':
                self.prev_direction = self.direction
                self.direction = 'UP'
                print(self.direction, self.prev_direction)

            if keys[pygame.K_DOWN] and self.direction != 'UP':
                self.prev_direction = self.direction
                self.direction = 'DOWN'
                print(self.direction, self.prev_direction)

            self._snake.move(direction=self.direction, prev_direction=self.prev_direction)
            #print(self._snake.coordinates)

            if self._checker.check_collision_with_self() or self._checker.check_collision_with_wall():
                self._snake.coordinates = np.array([[np.random.randint(0, ROWS - 1), np.random.randint(0, COLUMNS - 1)]])
                self.direction = np.random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
            
            if self._checker.check_collision_with_fruit():
                self._snake.grow()
                self._fruit.respawn(snake=self._snake.coordinates)

            screen.fill(color=COLORS['BLACK'])
            self._draw.draw_screen(self._snake.coordinates, self._fruit.position)
            pygame.display.update()


if __name__ == "__main__":
    Game().start()
    



