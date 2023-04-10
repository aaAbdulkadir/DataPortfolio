from script import *
import pandas as pd

# check if the output of load_dataset('titanic') is an instance of the pd.DataFrame class.
# If the output is not a DataFrame object, then the function returns False, and the test fails.
def test_load_dataset_returns_dataframe():
    assert isinstance(load_dataset('titanic'), pd.DataFrame)

def test_len_of_rows():
    assert len_of_rows(load_dataset('titanic')) == 891

def test_len_of_cols():
    assert len_of_cols(load_dataset('titanic')) == 15

def test_len_of_cols_with_different_dataset():
    df = load_dataset('tips')
    assert len_of_cols(df) == 7

def test_len_of_rows_with_subset():
    df = load_dataset('titanic')
    subset_df = df.loc[df['age'] < 18]
    assert len_of_rows(subset_df) == 113
