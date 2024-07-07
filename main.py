import pygame
from sys import exit
import random
import queue

pygame.init()  # Initializing pygame components

# Creating the window of size width * height
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# Neighbours
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def valid(x, y, n, m):
    """Check if a given position is within the grid boundaries."""
    return x >= 0 and y >= 0 and x < n and y < m

# Colors
BLACK = (0, 0, 0)  # Blocked cells
WHITE = (255, 255, 255)  # Free cells
RED = (255, 0, 0)  # Visited cells
GREEN = (0, 255, 0)  # Leaf cells
YELLOW = (255, 255, 0)  # Start
BLUE = (0, 0, 255)  # End
PURPLE = (128, 0, 128)  # Path

# Grid dimensions
ROWS = 20

class pair:
    """Class representing a pair of coordinates."""
    def __init__(self, x, y):
        self.first = x
        self.second = y

    def __str__(self):
        return f"pair({self.first}, {self.second})"

    def __repr__(self):
        return self.__str__()

class Spot:
    """Class representing a spot in the grid."""
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == BLUE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = YELLOW

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def __str__(self):
        return f"Spot({self.row}, {self.col})"

    def __repr__(self):
        return self.__str__()

def MakeGrid():
    """Create the initial grid with Spot objects."""
    grid = []
    gap = WIDTH // ROWS
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            spot = Spot(i, j, gap)
            grid[i].append(spot)
    return grid

def DrawGrid():
    """Draw the grid lines on the window."""
    GAP = WIDTH // ROWS
    i = 0
    while i * GAP < WIDTH:
        pygame.draw.line(WIN, "GRAY", (i * GAP, 0), (i * GAP, WIDTH))
        i += 1
    i = 0
    while i * GAP < WIDTH:
        pygame.draw.line(WIN, "GRAY", (0, i * GAP), (WIDTH, i * GAP))
        i += 1

def get_clicked_pos(pos):
    """Given mouse position, return the corresponding grid cell."""
    gap = WIDTH // ROWS
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

# Make grid and start and end
grid = MakeGrid()
start = None
end = None

# BFS data
vis = [[0] * ROWS for i in range(ROWS)]
dist = []
parent = []

def init_grid():
    """Initialize the grid and BFS data structures."""
    global start, end, grid, vis, dist
    start = None
    end = None
    for i in range(ROWS):
        for j in range(ROWS):
            grid[i][j].color = WHITE
    vis.clear()
    vis = [[0] * ROWS for i in range(ROWS)]
    dist.clear()
    for i in range(ROWS):
        temp = []
        temp2 = []
        for j in range(ROWS):
            temp2.append(pair(-1, -1))
            temp.append(pair(ROWS * ROWS * ROWS, 0))
        parent.append(temp2)
        dist.append(temp)

# Initializing the grid
init_grid()

clock = pygame.time.Clock()

def Run_Algorithm1():
    """Run BFS algorithm to find the shortest path."""
    global vis, dist, parent
    vis[start.row][start.col] = True
    dist[start.row][start.col].first = 0
    dist[start.row][start.col].second = 1
    q = queue.Queue()
    q.put(pair(start.row, start.col))
    while not q.empty():
        x = q.get()
        row = x.first
        col = x.second

        if not (row == start.row and col == start.col):
            grid[row][col].color = RED
        for i in range(4):
            ni = row + dx[i]
            nj = col + dy[i]
            if valid(ni, nj, ROWS, ROWS) and grid[ni][nj].color != BLACK and not vis[ni][nj]:
                if grid[ni][nj].color == BLUE:
                    dist[ni][nj].first = dist[row][col].first + 1
                    dist[ni][nj].second = dist[row][col].second
                    parent[ni][nj] = pair(row, col)
                    return
                grid[ni][nj].color = GREEN
                parent[ni][nj] = pair(row, col)
                vis[ni][nj] = True
                dist[ni][nj].first = dist[row][col].first + 1
                dist[ni][nj].second = dist[row][col].second
                q.put(pair(ni, nj))
            elif valid(ni, nj, ROWS, ROWS) and dist[ni][nj].first == 1 + dist[row][col].first:
                dist[ni][nj].second += dist[row][col].second
        draw()
        pygame.time.delay(20)

done = False

def Run_Algorithm2(node):
    """Run DFS algorithm to find the path."""
    global parent, vis, done

    vis[node.row][node.col] = True
    if node != start:
        grid[node.row][node.col].color = RED
    draw()
    temp = [0, 1, 2, 3]
    random.shuffle(temp)
    for i in temp:
        row = node.row
        col = node.col
        ni = row + dx[i]
        nj = col + dy[i]
        if valid(ni, nj, ROWS, ROWS) and grid[ni][nj].color != BLACK and not vis[ni][nj]:
            if done:
                return
            if grid[ni][nj].color == BLUE:
                dist[ni][nj].first = dist[row][col].first + 1
                dist[ni][nj].second = dist[row][col].second
                parent[ni][nj] = pair(row, col)
                done = True
                return
            grid[ni][nj].color = GREEN
            parent[ni][nj] = pair(row, col)
            draw()
            pygame.time.delay(20)
            if done:
                return
            Run_Algorithm2(grid[ni][nj])

def draw():
    """Draw the grid and update the display."""
    for i in range(ROWS):
        for j in range(ROWS):
            grid[i][j].draw(WIN)  # Drawing the grid
    DrawGrid()
    pygame.display.update()

clock = pygame.time.Clock()

StartMenu = True
BUTTON_COLOR = (0, 0, 255)
BUTTON_HOVER_COLOR = (0, 100, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

class Button:
    """Class representing a button in the start menu."""
    def __init__(self, text, pos, callback):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], 150, 50)
        self.color = BUTTON_COLOR

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = FONT.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()
            return True
        return False

    def update_color(self, pos):
        if self.rect.collidepoint(pos):
            self.color = BUTTON_HOVER_COLOR
        else:
            self.color = BUTTON_COLOR

# Callback functions
def dfs_callback():
    global StartMenu, algo
    StartMenu = False
    algo = "dfs"

def bfs_callback():
    global StartMenu, algo
    StartMenu = False
    algo = "bfs"

# Create buttons
dfs_button = Button("DFS", (WIDTH//2 - 175, WIDTH//2 - 25), dfs_callback)
bfs_button = Button("BFS", (WIDTH//2 + 25, WIDTH//2 - 25), bfs_callback)

algo = "bfs"
while True:  # Game main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        IN = False
        if StartMenu and pygame.mouse.get_pressed()[0]:
            IN = True
            if dfs_button.check_click(pygame.mouse.get_pos()):
                StartMenu = False
                algo = "dfs"
            elif bfs_button.check_click(pygame.mouse.get_pos()):
                StartMenu = False
                algo = "bfs"

        if not IN and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if algo == "bfs":
                    Run_Algorithm1()
                    while end.row != -1:
                        if grid[end.row][end.col].color == RED:
                            grid[end.row][end.col].color = PURPLE
                        draw()
                        x = parent[end.row][end.col]
                        end.row = x.first
                        end.col = x.second
                        pygame.time.delay(20)
                else:
                    Run_Algorithm2(start)
                    while end.row != -1:
                        if grid[end.row][end.col].color == RED:
                            grid[end.row][end.col].color = PURPLE
                        draw()
                        x = parent[end.row][end.col]
                        end.row = x.first
                        end.col = x.second
                        pygame.time.delay(20)

        if not IN and pygame.mouse.get_pressed()[0]:
            # Left click
            mouse_pos = pygame.mouse.get_pos()
            i, j = get_clicked_pos(mouse_pos)

            if not valid(i, j, ROWS, ROWS):  # Handle mouse out of the screen
                continue

            if start is None and end != grid[i][j] and grid[i][j].color == WHITE:  # Handle start and not override any cell
                start = grid[i][j]
                start.color = YELLOW

            elif end is None and start != grid[i][j] and grid[i][j].color == WHITE:
                end = grid[i][j]
                end.color = BLUE

            else:
                if grid[i][j] == start or grid[i][j] == end:
                    continue
                grid[i][j].color = BLACK

            grid[i][j].draw(WIN)

        if not IN and pygame.mouse.get_pressed()[2]:
            # Right click
            mouse_pos = pygame.mouse.get_pos()
            i, j = get_clicked_pos(mouse_pos)

            grid[i][j].color = WHITE
            grid[i][j].draw(WIN)

            if start == grid[i][j]:
                start = None
            if end == grid[i][j]:
                end = None

    if StartMenu:
        pygame.display.set_caption("DFS and BFS Buttons")
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                dfs_button.check_click(pos)
                bfs_button.check_click(pos)

        pos = pygame.mouse.get_pos()
        dfs_button.update_color(pos)
        bfs_button.update_color(pos)

        dfs_button.draw(WIN)
        bfs_button.draw(WIN)
        pygame.display.flip()
    else:
        draw()
        clock.tick(30)
