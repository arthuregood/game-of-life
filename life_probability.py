from gameoflife import GameofLife
import numpy as np
import csv

header = ['probability', 'generations', 'population_size', 'result']
average = []
zero_reference = [0, 0, 0, 0]

with open('life_analysis.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for probability in range(101):
        data = []
        for times in range(10):
            gol = GameofLife(life_probability=probability)
            gol.main(10)
            data.append([probability, gol.generations,
                        gol.population_size, gol.result])
        print(data)
        writer.writerows(data)
        average.append(list(map(lambda x: sum(x)/len(x), zip(*data))))

with open('average_analysis.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerows(average)
