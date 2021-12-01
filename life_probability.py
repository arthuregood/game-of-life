from gameoflife import GameofLife
from os.path import exists
import os
import numpy as np
import csv


# disable video render
os.environ["SDL_VIDEODRIVER"] = "dummy"

header = ['probability', 'generations', 'population_size', 'result']

# check if file exists
file_exists = exists('life_analysis.csv')
if not file_exists:
    with open('life_analysis.csv', 'w', encoding='UTF8') as f:

        writer = csv.writer(f)
        writer.writerow(header)

for probability in range(0, 101):
    for times in range(10):
        gol = GameofLife(life_probability=probability)
        gol.main(10)
        data = []
        data.append([probability, gol.generations,
                    gol.population_size, gol.result])
        print(data)

        with open('life_analysis.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
