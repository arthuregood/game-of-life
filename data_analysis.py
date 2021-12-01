from os.path import exists
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


# check if file exists
file_exists = exists('life_analysis.csv')
median = True
savetype = 'total'

if file_exists:
    df = pd.read_csv('life_analysis.csv')

    if median:
        df = df.groupby(np.arange(len(df))//10)
        savetype = 'median'

    data = [('generations', 'Generations Analysis'),
            ('population_size', 'Population Analysis')]

    for y, title in data:

        df.boxplot('probability', y)
        plt.xticks(range(0, 101, 10), range(0, 101, 10))
        plt.title(title)
        plt.gcf().set_size_inches(19.2, 10.8)
        plt.savefig(fname=f'results/{y}')
        plt.show()
