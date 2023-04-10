from script import *
import pandas as pd
from matplotlib.testing.compare import compare_images
import numpy as np
import os

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

def test_age_in_dataset():
    df = load_dataset('titanic')
    age_to_check = 22
    assert age_to_check in df['age'].values

def test_unique_id_column():
    df = load_dataset('titanic')
    assert 'unique_id' not in df.columns

def test_duplicate_rows():
    df = load_dataset('titanic')
    num_duplicates = df.duplicated().sum()
    assert num_duplicates == 107

def test_expected_column_data_types():
    df = load_dataset('titanic')
    expected_data_types = {'survived': 'int64', 'age': 'float64', 'class': 'category'}
    for col_name, expected_type in expected_data_types.items():
        assert str(df[col_name].dtype) == expected_type

def test_min_num_rows():
    df = load_dataset('titanic')
    min_num_rows = 500
    assert len_of_rows(df) >= min_num_rows, "If failed, this message will run"

def test_plot_bar_chart_titanic():
    # Generate the test data
    df = load_dataset('titanic')
    var1 = 'class'
    var2 = 'fare'

    # Generate the expected image
    plt.bar(df[var1], df[var2])
    expected_file = 'expected_bar_chart.png'
    plt.savefig(expected_file)

    # Generate the actual image
    actual_file = 'actual_bar_chart.png'
    plot_bar_chart(df, var1, var2)
    plt.savefig(actual_file)

    # Compare the images
    is_same = compare_images(expected_file, actual_file, tol=1e-3)
    assert is_same

    # Clean up the image files
    os.remove(expected_file)
    os.remove(actual_file)