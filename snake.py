from globals import *
import pygame

class Snake:

    def __init__(self) -> None:
        self.coordinates = np.array([[ROWS//2, COLUMNS//2],
                                     [ROWS//2 - 1, COLUMNS//2],
                                     [ROWS//2 - 2, COLUMNS//2]]
                                     )
        

    def move(self,direction, prev_direction) -> None:

        if direction == 'RIGHT' and prev_direction != 'LEFT':
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 0] += 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'LEFT' and prev_direction != 'RIGHT':
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 0] -= 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'UP' and prev_direction != 'DOWN':
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 1] -= 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]
        elif direction == 'DOWN' and prev_direction != 'UP':
            snake_copy = self.coordinates.copy()
            self.coordinates[0, 1] += 1
            for i in range(1, len(self.coordinates)):
                self.coordinates[i] = snake_copy[i - 1]


    def grow(self) -> None:
        self.coordinates = np.vstack((self.coordinates, self.coordinates[-1]))


