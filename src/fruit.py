from globals import *
import random

class Fruit():

    def __init__(self) -> None:
        self.position = [10, 8]
        

    def respawn(self, snake) -> None:
        """
        Respawn the fruit at a random location on the game board that is not 
        occupied by the snake.

        Args:
            snake (numpy.ndarray): The snake's coordinates.
        """
        while True:
            x_coordinate = random.randint(0, ROWS - 1)
            y_coordinate = random.randint(0, COLUMNS - 1)

            if x_coordinate not in snake[:, 0] and y_coordinate not in snake[:, 1]:
                break

        self.position = [x_coordinate, y_coordinate]
            