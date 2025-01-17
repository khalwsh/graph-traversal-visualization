import pygame
from constants.colors import WHITE
from constants.settings import WIDTH, ROWS
from components.spot import Spot

class Grid:
    def __init__(self):
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []
        gap = WIDTH // ROWS
        for i in range(ROWS):
            grid.append([])
            for j in range(ROWS):
                spot = Spot(i, j, gap)
                grid[i].append(spot)
        return grid

    def draw_grid_lines(self, win):
        gap = WIDTH // ROWS
        for i in range(ROWS):
            pygame.draw.line(win, "GRAY", (i * gap, 0), (i * gap, WIDTH))
            pygame.draw.line(win, "GRAY", (0, i * gap), (WIDTH, i * gap))

    def draw(self, win, init=False):
        win.fill(WHITE)
        for row in self.grid:
            for spot in row:
                if init:
                    spot.reset()
                spot.draw(win)
        self.draw_grid_lines(win)
        pygame.display.update()

    def get_clicked_pos(self, pos):
        gap = WIDTH // ROWS
        y, x = pos
        row = y // gap
        col = x // gap
        return row, col