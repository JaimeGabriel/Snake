from globals import *
import pygame
import numpy as np

class Snake:

    def __init__(self) -> None:
        self.coordinates = np.array([[ROWS//2, COLUMNS//2],
                                     [ROWS//2 - 1, COLUMNS//2],
                                     [ROWS//2 - 2, COLUMNS//2]]
                                     )
        

    def move(self, direction, prev_direction) -> None:
        """
        Updates the coordinates of the snake according to the given direction.

        Args:
            direction (str): The direction the snake is moving.
            prev_direction (str): The previous direction the snake was moving.

        Returns:
            None
        """
        if direction == 'RIGHT' and prev_direction != 'LEFT' and self.coordinates[0, 1] < COLUMNS - 1:
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 1] += 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'LEFT' and prev_direction != 'RIGHT' and self.coordinates[0, 1] > 0:
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 1] -= 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'UP' and prev_direction != 'DOWN' and self.coordinates[0, 0] > 0:
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 0] -= 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'DOWN' and prev_direction != 'UP' and self.coordinates[0, 0] < ROWS - 1:
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 0] += 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]


    def grow(self) -> None:
        self.coordinates = np.vstack((self.coordinates, self.coordinates[-1]))


