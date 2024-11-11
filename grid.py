# grid.py
import pygame
from colors import *
from spot import Spot
import settings

# Define the window and grid dimensions
WIDTH = settings.WIDTH
ROWS = settings.ROWS
WIN = pygame.display.set_mode((WIDTH, WIDTH))

def make_grid():
    """Create the initial grid with Spot objects."""
    grid = []
    gap = WIDTH // ROWS
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            spot = Spot(i, j, gap)
            grid[i].append(spot)
    return grid

def draw_grid_lines():
    """Draw the grid lines on the window."""
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(WIN, "GRAY", (i * gap, 0), (i * gap, WIDTH))
        pygame.draw.line(WIN, "GRAY", (0, i * gap), (WIDTH, i * gap))

def draw(grid):
    """Draw the grid and update the display."""
    WIN.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(WIN)
    draw_grid_lines()
    pygame.display.update()

def get_clicked_pos(pos):
    """Given mouse position, return the corresponding grid cell."""
    gap = WIDTH // ROWS
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
