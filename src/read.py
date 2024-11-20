import pandas as pd

from globals import *

class Read():

    def __init__(self) -> None:
        pass

    def read_top_scores(self, filename_top_scores) -> tuple[list, list]:
        """ Reads the top scores from the csv file.

        Args:
            filename_top_scores (str): The name of the csv file.

        Returns:
            tuple[list, list]: The top scores and the names of the players. 
        """
        print('read')
        top_scores_dataframe = pd.read_csv(filename_top_scores).sort_values(by='score', ascending=False).head(3)
        return top_scores_dataframe.values.tolist()
    
    