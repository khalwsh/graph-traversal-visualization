import pygame

BUTTON_COLOR = (0, 0, 255)
BUTTON_HOVER_COLOR = (0, 100, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

class Button:
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

def dfs_callback():
    global StartMenu, algo
    StartMenu = False
    algo = "dfs"

def bfs_callback():
    global StartMenu, algo
    StartMenu = False
    algo = "bfs"
