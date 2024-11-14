import pandas as pd

from globals import *
from draw import Draw

class Read():

    def __init__(self) -> None:
        self._draw = Draw()
        pass

    def read_top_scores(self, filename_top_scores) -> tuple[list, list]:
        """ Read the top scores from the csv file """
        
        top_scores_dataframe = pd.read_csv(filename_top_scores).sort_values(by='score', ascending=False).head(3)
        return top_scores_dataframe.values.tolist()
    
    def draw_game_screen(self, snake_coordinates, fruit_position, score):
        """"Draw all elements on the game screen"""

        screen.fill(color=COLORS['BLACK'])
        self._draw.draw_game_screen(snake_coordinates, fruit_position)
        self._draw.draw_score_frame()
        self._draw.draw_live_score(score)
        self._draw.draw_ascii_art()
        if self.read_top_scores:
            self.top_scores_list = self.read_top_scores('player_data/top_scores.csv')
        self._draw.draw_top_scores(self.top_scores_list)
        self.read_top_scores_bool = False