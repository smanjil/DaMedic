
import pandas as pd

from config import FILE_PATH
from utils import read_files


class CSVJoiner(object):
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2

    def join_dfs(self):
        print (self.df1.head())
        print (self.df2.head())


if __name__ == '__main__':
    # read both csv files
    df1, df2 = read_files(FILE_PATH)

    # instantiate CSVJoiner class
    csvjoin = CSVJoiner(df1, df2)
    csvjoin.join_dfs()
