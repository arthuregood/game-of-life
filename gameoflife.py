import pygame as pg
import numpy as np


# colours
cell_alive = (255, 255, 215)
cell_to_die = (200, 200, 225)
background = (10, 10, 40)
grid = (30, 30, 60)

width, height = 90, 90


# randomize the grid
def random_cells():
    cells = np.random.randint(2, size=(width, height))
    return(cells)


# updates the grid
def update(screen, cz, cells):
    next = np.zeros((cells.shape[0], cells.shape[1]))

    for r, c in np.ndindex(cells.shape):
        num_alive = np.sum(cells[r-1:r+2, c-1:c+2]) - cells[r, c]

        if cells[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = cell_to_die
        elif (cells[r, c] == 1 and 2 <= num_alive <= 3) or (cells[r, c] == 0 and num_alive == 3):
            next[r, c] = 1
            col = cell_alive

        col = col if cells[r, c] == 1 else background
        pg.draw.rect(screen, col, (c*cz, r*cz, cz-1, cz-1))

    return next


def main(cz):
    pg.init()
    pg.display.set_caption(
        "Game of Life by arthuregood - Press R for Random :)")

    screen = pg.display.set_mode((width*cz, height*cz))
    cells = random_cells()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                cells = random_cells()

        cells = update(screen, cz, cells)
        pg.display.update()


if __name__ == "__main__":
    main(10)
