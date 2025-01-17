import sys

import pygame

from algorithms.bfs import run_bfs
from algorithms.dfs import run_dfs
from components.grid import Grid
from constants.colors import WHITE, BLACK, GREEN, BLUE
from constants.settings import WIDTH, ROWS
from utils.helpers import reset_grid

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualization")

def main():
    grid = Grid()
    start = None
    end = None
    algo = None
    parent = None
    done = False

    def draw_buttons():
        WIN.fill(WHITE)
        font = pygame.font.SysFont("Arial", 30)
        bfs_text = font.render("BFS", True, BLACK)
        dfs_text = font.render("DFS", True, BLACK)

        bfs_button = pygame.Rect(WIDTH // 4 - 75, WIDTH // 2 - 30, 150, 60)
        dfs_button = pygame.Rect(3 * WIDTH // 4 - 75, WIDTH // 2 - 30, 150, 60)

        pygame.draw.rect(WIN, GREEN, bfs_button)
        pygame.draw.rect(WIN, BLUE, dfs_button)

        WIN.blit(bfs_text, (bfs_button.x + 50, bfs_button.y + 15))
        WIN.blit(dfs_text, (dfs_button.x + 50, dfs_button.y + 15))

        pygame.display.update()
        return bfs_button, dfs_button

    clock = pygame.time.Clock()
    run = True
    start_menu = True

    while run:
        if start_menu:
            bfs_button, dfs_button = draw_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if bfs_button.collidepoint(pos):
                        algo = "bfs"
                        start_menu = False
                    elif dfs_button.collidepoint(pos):
                        algo = "dfs"
                        start_menu = False

        else:
            grid.draw(WIN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if pygame.mouse.get_pressed()[0]:  # Left click
                    pos = pygame.mouse.get_pos()
                    row, col = grid.get_clicked_pos(pos)

                    if 0 <= row < ROWS and 0 <= col < ROWS:
                        if grid.grid[row][col].color == WHITE:
                            if start is None:
                                start = grid.grid[row][col]
                                start.make_start()
                            elif end is None:
                                end = grid.grid[row][col]
                                end.make_end()
                            else:
                                grid.grid[row][col].make_barrier()

                elif pygame.mouse.get_pressed()[2]:  # Right click
                    pos = pygame.mouse.get_pos()
                    row, col = grid.get_clicked_pos(pos)
                    grid.grid[row][col].reset()
                    if grid.grid[row][col] == start:
                        start = None
                    elif grid.grid[row][col] == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if done:
                        reset_grid(grid.grid)
                        start = None
                        end = None
                        algo = None
                        parent = None
                        done = False
                        start_menu = True
                        continue
                    if event.key == pygame.K_SPACE and start and end:
                        if algo == "bfs":
                            parent = run_bfs(start, end, grid.grid, lambda: grid.draw(WIN))
                        elif algo == "dfs":
                            parent = run_dfs(start, end, grid.grid, lambda: grid.draw(WIN))

                        if parent:
                            node = (end.row, end.col)
                            while node:
                                if node != (start.row, start.col) and node != (end.row, end.col):
                                    grid.grid[node[0]][node[1]].make_path()
                                pygame.time.delay(30)
                                node = parent[node[0]][node[1]]
                                grid.draw(WIN)
                        done = True

        clock.tick(30)

if __name__ == "__main__":
    main()