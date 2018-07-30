
import os
import pandas as pd

from config import FILE_PATH
from utils import read_files


class CSVJoiner(object):
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2

    def join_dfs(self):
        def get_id_val_df2(row):
            return self.df2[self.df2['id'] == row]['val2'].values

        self.df1['val2'] = self.df1['id'].apply(get_id_val_df2)

    def get_json(self):
        if 'output_file' not in os.listdir(FILE_PATH):
            os.mkdir('output_file')
        self.df1.to_json('/'.join([FILE_PATH, 'output_file/result.json']), orient = 'records')


if __name__ == '__main__':
    # read both csv files
    df1, df2 = read_files(FILE_PATH)

    # instantiate CSVJoiner class
    csvjoin = CSVJoiner(df1, df2)
    csvjoin.join_dfs()
    csvjoin.get_json()
