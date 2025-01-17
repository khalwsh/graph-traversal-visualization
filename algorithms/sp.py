from collections import deque
from constants.settings import DX, DY, ROWS
from constants.colors import BLACK, GREEN, BLUE, RED

def run_sp(start, end, grid):
    # Initialize vis array: (shortest_path_length, count_of_shortest_paths)
    vis = [[(float('inf'), 0)] * ROWS for _ in range(ROWS)]
    vis[start.row][start.col] = (0, 1)  # Start cell has shortest_path_length = 0 and count = 1

    q = deque([(start.row, start.col)])

    while q:
        row, col = q.popleft()

        for i in range(4):
            ni, nj = row + DX[i], col + DY[i]
            if 0 <= ni < ROWS and 0 <= nj < ROWS and vis[row][col][0] + 1 <= vis[ni][nj][0] and not grid[ni][nj].is_obstacle():
                new_length = vis[row][col][0] + 1

                if new_length < vis[ni][nj][0]:
                    vis[ni][nj] = (new_length, vis[row][col][1])
                    q.append((ni, nj))

                elif new_length == vis[ni][nj][0]:
                    vis[ni][nj] = (new_length, vis[ni][nj][1] + vis[row][col][1])

    return vis[end.row][end.col][1]