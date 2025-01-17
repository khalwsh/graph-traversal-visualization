import random
import pygame
from constants.settings import DX, DY, ROWS
from constants.colors import BLACK, GREEN, BLUE, RED

def run_dfs(start, end, grid, draw):
    vis = [[False] * ROWS for _ in range(ROWS)]
    parent = [[None] * ROWS for _ in range(ROWS)]
    stack = [(start.row, start.col)]

    while stack:
        row, col = stack.pop()

        if (row, col) == (end.row, end.col):
            return parent

        if not vis[row][col]:
            vis[row][col] = True
            if not (row == start.row and col == start.col):
                grid[row][col].color = RED
            draw()
            pygame.time.delay(20)

            neighbors = [(row + DX[i], col + DY[i]) for i in range(4)]
            random.shuffle(neighbors)
            for ni, nj in neighbors:
                if 0 <= ni < ROWS and 0 <= nj < ROWS and not vis[ni][nj] and grid[ni][nj].color != BLACK:
                    stack.append((ni, nj))
                    parent[ni][nj] = (row, col)
                    if grid[ni][nj].color == BLUE:
                        return parent
                    grid[ni][nj].color = GREEN

    return None