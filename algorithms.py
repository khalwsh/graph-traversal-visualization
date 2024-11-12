# algorithms.py
import pygame
import queue
import random
from colors import *
from spot import Spot
from settings import *

class Pair:
    """Class representing a pair of coordinates."""
    def __init__(self, x, y):
        self.first = x
        self.second = y
    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

def valid(x, y, n, m):
    """Check if a given position is within the grid boundaries."""
    return 0 <= x < n and 0 <= y < m

def run_bfs(start, end, grid, draw):
    """Run BFS algorithm to find the shortest path."""
    vis = [[False] * ROWS for _ in range(ROWS)]
    dist = [[float('inf')] * ROWS for _ in range(ROWS)]
    parent = [[None] * ROWS for _ in range(ROWS)]

    vis[start.row][start.col] = True
    dist[start.row][start.col] = 0
    q = queue.Queue()
    q.put(Pair(start.row, start.col))

    while not q.empty():
        node = q.get()
        row, col = node.first, node.second

        if not (row == start.row and col == start.col):
            grid[row][col].color = RED

        for i in range(4):
            ni, nj = row + dx[i], col + dy[i]
            if valid(ni, nj, ROWS, ROWS) and not vis[ni][nj] and grid[ni][nj].color != BLACK:
                if grid[ni][nj].color == BLUE:
                    parent[ni][nj] = Pair(row, col)
                    return parent
                vis[ni][nj] = True
                grid[ni][nj].color = GREEN
                parent[ni][nj] = Pair(row, col)
                q.put(Pair(ni, nj))

        draw()
        pygame.time.delay(10)

    return None

def run_dfs(start, end, grid, draw):
    """Run DFS algorithm to find the path."""
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

            neighbors = [(row + dx[i], col + dy[i]) for i in range(4)]
            random.shuffle(neighbors)
            for ni, nj in neighbors:
                if valid(ni, nj, ROWS, ROWS) and not vis[ni][nj] and grid[ni][nj].color != BLACK:
                    stack.append((ni, nj))
                    parent[ni][nj] = Pair(row, col)
                    if grid[ni][nj].color == BLUE:
                        return parent
                    grid[ni][nj].color = GREEN

    return None
