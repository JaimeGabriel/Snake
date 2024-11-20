from globals import *
from snake import Snake
from fruit import Fruit

class Checker(Snake, Fruit):

    def __init__(self, snake: Snake, fruit: Fruit) -> None:
        self.snake = snake
        self.fruit = fruit

    def check_collision_with_fruit(self) -> bool:
        """
        Checks if the snake head collided with the fruit.
        
        Returns:
            bool: True if there is a collision, False if there is no collision.
        """
        if self.snake.coordinates[0][0] == self.fruit.position[0] and self.snake.coordinates[0][1] == self.fruit.position[1]:
            return True
        return False
    
    def _check_collision_with_self(self) -> bool:
        """
        Checks if the snake head collided with itself.
        
        Returns:
            bool: True if there is a collision, False if there is no collision.
        """
        for i in range(1, len(self.snake.coordinates)):
            if self.snake.coordinates[0][0] == self.snake.coordinates[i][0] and self.snake.coordinates[0][1] == self.snake.coordinates[i][1]:
                return True
        return False
    
    def _check_collision_with_wall(self, direction) -> bool:
        """
        Checks if the snake head collided with a wall.
        
        Args:
            direction (str): The direction the snake is moving.
        
        Returns:
            bool: True if there is a collision, False if there is no collision.
        """
        if (self.snake.coordinates[0][1] == 0 and direction == 'LEFT') \
            or (self.snake.coordinates[0][1] == COLUMNS - 1 and direction == 'RIGHT') \
            or (self.snake.coordinates[0][0] == 0 and direction == 'UP') \
            or (self.snake.coordinates[0][0] == ROWS - 1 and direction == 'DOWN'):

            return True
        return False
    
    def check_collision(self, direction) -> bool:
        """
        Checks for collisions that end the game (snake or wall).
        
        Args:
            direction (str): The direction the snake is moving.
        
        Returns:
            bool: True if there is a collision, False if there is no collision.
        """
        if self._check_collision_with_self() or self._check_collision_with_wall(direction):
            return True
        return False
                
                
    

    


        



