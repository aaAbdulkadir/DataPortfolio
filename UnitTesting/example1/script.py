import seaborn as sns
from matplotlib import pyplot as plt

def load_dataset(file_path):
    return sns.load_dataset(file_path)

def print_dataset(df):
    print(df.head())

def len_of_rows(df):
    return df.shape[0]

def len_of_cols(df):
    return df.shape[1]

print_dataset(load_dataset('titanic'))

def plot_bar_chart(df, var1, var2):
    plt.bar(df[var1], df[var2])
    plt.show()

plot_bar_chart(load_dataset('titanic'), 'class', 'fare')