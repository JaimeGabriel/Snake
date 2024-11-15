import pandas as pd

from globals import *

class Read():

    def __init__(self) -> None:
        pass

    def read_top_scores(self, filename_top_scores) -> tuple[list, list]:
        """ Read the top scores from the csv file """
        
        top_scores_dataframe = pd.read_csv(filename_top_scores).sort_values(by='score', ascending=False).head(3)
        return top_scores_dataframe.values.tolist()
    
    