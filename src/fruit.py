from globals import *
import numpy as np

class Fruit():

    def __init__(self) -> None:
        self.position = np.array([10, 8])
        

    def respawn(self, snake) -> None:
        while True:
            x_coordinate = np.random.randint(low=0, high=ROWS - 1)
            y_coordinate = np.random.randint(low=0, high=COLUMNS - 1)

            if x_coordinate not in snake[:, 0] and y_coordinate not in snake[:, 1]:
                break

        self.position = np.array([x_coordinate, y_coordinate])
            