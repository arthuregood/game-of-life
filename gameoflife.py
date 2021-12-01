# concept by John Horton Conway
# implementation by arthuregood

import pygame as pg
import numpy as np
from math import sqrt
# colours
cell_alive = (255, 255, 215)
cell_to_die = (200, 200, 225)
background = (10, 10, 40)


class GameofLife:
    def __init__(self, life_probability):
        # user variables
        self.gamemode = False
        self.width = 90
        self.height = 90
        self.total_elements = self.width*self.height
        self.life_probability = life_probability
        self.generations = 0
        self.population_size = 0
        self.stability_list = []
        self.result = 0
        self.diagonal = int(sqrt((self.width**2)+(self.height**2)))

    # randomize the grid

    def random_cells(self):
        cells = np.random.choice(
            np.arange(0, 2), p=[(100-self.life_probability)/100, self.life_probability/100], size=(self.width, self.height))
        self.generations = 0
        self.stability_list = []
        return(cells)

    def stability_check(self, cells, next):
        number_of_equal_elements = np.sum(cells == next)
        self.generations += 1

        # check for unpredictably small values that
        # ​can break the verification, than resets
        if self.generations > 10000:
            return False

        percentage = number_of_equal_elements/self.total_elements

        self.stability_list.append(percentage)
        self.stability_list = self.stability_list[-self.diagonal:]

        # to check stability, here we check if anything happens in the meantime that
        # a single point could potentially cross the intire grid in the diagonal,
        # the longest line in our little world

        if len(self.stability_list) == self.diagonal and np.all(self.stability_list == self.stability_list[0]):
            result = 1
            if np.all(cells == 0):
                result = 0
            self.result = result
            self.population_size = np.sum(cells == 1)
            self.generations -= self.diagonal
            return True
    # updates the grid

    def update(self, screen, cz, cells):
        # next grid set of cells
        next = np.zeros((cells.shape[0], cells.shape[1]))
        # compare cells with their neighbors
        for r, c in np.ndindex(cells.shape):
            num_alive = np.sum(cells[r-1:r+2, c-1:c+2]) - cells[r, c]

            if cells[r, c] == 1 and num_alive < 2 or num_alive > 3:
                col = cell_to_die
            elif (cells[r, c] == 1 and 2 <= num_alive <= 3) or (cells[r, c] == 0 and num_alive == 3):
                next[r, c] = 1
                col = cell_alive

            col = col if cells[r, c] == 1 else background
            pg.draw.rect(screen, col, (c*cz, r*cz, cz-1, cz-1))

        if not self.gamemode:
            if self.stability_check(cells, next) is True:
                return False
            elif self.stability_check(cells, next) is False:
                return self.random_cells()

        return next

    def main(self, cz):
        pg.init()
        pg.display.set_caption(
            "Game of Life by arthuregood - Press R for Random :)")

        screen = pg.display.set_mode((self.width*cz, self.height*cz))
        cells = self.random_cells()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    cells = self.random_cells()

            cells = self.update(screen, cz, cells)
            if type(cells) != np.ndarray:
                pg.quit()
                return
            pg.display.update()


if __name__ == "__main__":
    gameoflife = GameofLife(20)
    gameoflife.main(10)
