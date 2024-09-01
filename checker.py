from globals import *
import pygame
import numpy as np
from snake import Snake
from fruit import Fruit

class Checker(Snake, Fruit):

    def __init__(self, snake: Snake, fruit: Fruit) -> None:
        # Store references to snake and fruit objects
        self.snake = snake
        self.fruit = fruit

    def check_collision_with_fruit(self) -> bool:
        if self.snake.coordinates[0, 0] == self.fruit.position[0] and self.snake.coordinates[0, 1] == self.fruit.position[1]:
            print('collision')

            return True
        return False
    
    def check_collision_with_self(self) -> bool:
        for i in range(1, len(self.snake.coordinates)):
            if self.snake.coordinates[0, 0] == self.snake.coordinates[i, 0] and self.snake.coordinates[0, 1] == self.snake.coordinates[i, 1]:
                return True
        return False
    
    def check_collision_with_wall(self) -> bool:
        if self.snake.coordinates[0, 0] < 0 or self.snake.coordinates[0, 0] == COLUMNS or self.snake.coordinates[0, 1] < 0 or self.snake.coordinates[0, 1] == ROWS:
            return True
        return False

        



