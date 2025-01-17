import pygame
from collections import deque
from constants.settings import DX, DY, ROWS
from constants.colors import BLACK, GREEN, BLUE, RED

def run_bfs(start, end, grid, draw):
    vis = [[False] * ROWS for _ in range(ROWS)]
    parent = [[None] * ROWS for _ in range(ROWS)]
    q = deque([(start.row, start.col)])
    vis[start.row][start.col] = True

    while q:
        row, col = q.popleft()

        if (row, col) == (end.row, end.col):
            return parent

        for i in range(4):
            ni, nj = row + DX[i], col + DY[i]
            if 0 <= ni < ROWS and 0 <= nj < ROWS and not vis[ni][nj] and grid[ni][nj].color != BLACK:
                vis[ni][nj] = True
                parent[ni][nj] = (row, col)
                if grid[ni][nj].color == BLUE:
                    return parent
                grid[ni][nj].color = GREEN
                q.append((ni, nj))
        if not ((row == end.row and col == end.col) or (row == start.row and col == start.col)):
            grid[row][col].color = RED

        draw()
        pygame.time.delay(10)

    return None