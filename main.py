# main.py
import pygame
import sys
from grid import make_grid, draw, get_clicked_pos
from algorithms import run_bfs, run_dfs, Pair
from colors import WHITE, BLACK, GREEN, BLUE
from settings import WIDTH, ROWS

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualization")

grid = make_grid()
start = None
end = None
algo = None

def draw_buttons():
    """Draw the BFS and DFS selection buttons on the screen."""
    WIN.fill(WHITE)

    font = pygame.font.SysFont("Arial", 30)
    bfs_text = font.render("BFS", True, BLACK)
    dfs_text = font.render("DFS", True, BLACK)

    # Button positions and dimensions
    bfs_button = pygame.Rect(WIDTH // 4 - 75, WIDTH // 2 - 30, 150, 60)
    dfs_button = pygame.Rect(3 * WIDTH // 4 - 75, WIDTH // 2 - 30, 150, 60)

    # Draw buttons
    pygame.draw.rect(WIN, GREEN, bfs_button)
    pygame.draw.rect(WIN, BLUE, dfs_button)

    # Render text onto buttons
    WIN.blit(bfs_text, (bfs_button.x + 50, bfs_button.y + 15))
    WIN.blit(dfs_text, (dfs_button.x + 50, dfs_button.y + 15))

    pygame.display.update()
    return bfs_button, dfs_button

def main():
    global start, end, algo , grid
    clock = pygame.time.Clock()
    run = True
    start_menu = True

    while run:
        if start_menu:
            bfs_button, dfs_button = draw_buttons()  # Draw buttons and get their rects

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Check if BFS or DFS button was clicked
                    if bfs_button.collidepoint(pos):
                        algo = "bfs"
                        start_menu = False
                    elif dfs_button.collidepoint(pos):
                        algo = "dfs"
                        start_menu = False

        else:
            draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if pygame.mouse.get_pressed()[0]:  # Left click
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos)

                    if grid[row][col].color == WHITE:
                        if start is None:
                            start = grid[row][col]
                            start.make_start()
                        elif end is None:
                            end = grid[row][col]
                            end.make_end()
                        else:
                            grid[row][col].make_barrier()

                elif pygame.mouse.get_pressed()[2]:  # Right click
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos)
                    grid[row][col].reset()
                    if grid[row][col] == start:
                        start = None
                    elif grid[row][col] == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        if algo == "bfs":
                            parent = run_bfs(start, end, grid, lambda: draw(grid))
                        elif algo == "dfs":
                            parent = run_dfs(start, end, grid, lambda: draw(grid))

                        # Trace back path
                        if parent:
                            node = Pair(end.row, end.col)
                            while node:
                                grid[node.first][node.second].make_path()
                                node = parent[node.first][node.second]
                            draw(grid)

                    elif event.key == pygame.K_r:  # Reset grid
                        start = None
                        end = None
                        algo = None
                        grid = make_grid()
                        start_menu = True

        clock.tick(30)

if __name__ == "__main__":
    main()
