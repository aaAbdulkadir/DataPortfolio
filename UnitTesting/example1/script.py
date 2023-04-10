import seaborn as sns

def load_dataset(file_path):
    return sns.load_dataset(file_path)

def print_dataset(df):
    print(df.head())

def len_of_rows(df):
    return df.shape[0]

def len_of_cols(df):
    return df.shape[1]
