from os.path import exists
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

class Visualization:

  def start(self):
    # check if file exists
    file_path = 'data_analysis/life_probability.csv'
    file_exists = exists(file_path)

    if file_exists:
        df = pd.read_csv(file_path)
        df = df.groupby(np.arange(len(df))//10)

        data = [('generations', 'Generations Analysis'),
                ('population_size', 'Population Analysis')]

        for y, title in data:

            df.boxplot('probability', y)
            plt.xticks(range(0, 101, 10), range(0, 101, 10))
            plt.title(title)
            plt.gcf().set_size_inches(19.2, 10.8)
            plt.savefig(fname=f'data_analysis/results/{y}')
            plt.show()
