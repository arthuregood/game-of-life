from gameoflife import GameofLife
from os.path import exists
import numpy as np
import csv


header = ['probability', 'generations', 'population_size', 'result']

# check if file exists
file_exists = exists('life_analysis.csv')
if not file_exists:
    with open('life_analysis.csv', 'w', encoding='UTF8') as f:

        writer = csv.writer(f)
        writer.writerow(header)

for probability in range(14, 15):
    data = []
    for times in range(1):
        gol = GameofLife(life_probability=probability)
        gol.main(10)
        data.append([probability, gol.generations,
                    gol.population_size, gol.result])
    print(data)
    with open('life_analysis.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
