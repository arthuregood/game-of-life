from os.path import exists
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


# check if file exists
file_exists = exists('life_analysis.csv')

if file_exists:
    df = pd.read_csv('life_analysis.csv')
    df = df.groupby(np.arange(len(df))//10).mean()

    data = [('generations', 'Generations Analysis'),
            ('population_size', 'Population Analysis')]

    for y, title in data:
        df.plot(kind='bar', x='probability', y=y, title=title)
        plt.gcf().set_size_inches(19.2, 10.8)
        plt.savefig(fname=f'results/{y}')
