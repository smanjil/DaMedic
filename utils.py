
import os
import pandas as pd


def read_files(FILE_PATH):
    df1 = pd.read_csv(os.path.join(FILE_PATH, 'input_files/first.csv'))
    df2 = pd.read_csv(os.path.join(FILE_PATH, 'input_files/second.csv'))

    return df1, df2
