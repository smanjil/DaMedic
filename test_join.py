
import pandas as pd

from main import CSVJoiner

# prepare two dataframes for test
df1 = pd.DataFrame({'id': pd.Series([1, 2, 3]), 'val1': pd.Series([44, 645, 3423])})
df2 = pd.DataFrame({'id': pd.Series([1, 1, 1, 2, 2, 3]), 'val2': pd.Series([22, 44, 34, 45, 41, 44])})

# instantiate object
csvobj = CSVJoiner(df1, df2)

# join result
result_df = pd.DataFrame({'id': pd.Series([1, 2, 3]), 'val1': pd.Series([44, 645, 3423]), 'val2': pd.Series([[22, 44, 34], [45, 41], [44]])})

def test_check_join():
    csvobj.join_dfs()

    csvobj_df1_vals = list(map(lambda x: list(x), csvobj.df1['val2'].values))
    result_df_vals = list(map(lambda x: list(x), result_df['val2'].values))

    assert csvobj_df1_vals == result_df_vals
