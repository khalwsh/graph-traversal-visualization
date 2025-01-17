import sys

import pygame

def reset_grid(grid):
    for row in grid:
        for spot in row:
            spot.reset()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
POPUP_WIDTH, POPUP_HEIGHT = 190, 50
SCROLLBAR_HEIGHT = 10
FONT_SIZE = 24
FONT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
POPUP_COLOR = (200, 200, 200)
SCROLLBAR_COLOR = (100, 100, 100)

def draw_popup(text, screen):
    text = "  #Shortest paths: " + text
    while True:
        popup_rect = pygame.Rect(
            (SCREEN_WIDTH - POPUP_WIDTH) // 2,
            (SCREEN_HEIGHT - POPUP_HEIGHT) // 2,
            POPUP_WIDTH,
            POPUP_HEIGHT
        )
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(text, True, FONT_COLOR)
        text_width, text_height = text_surface.get_size()

        if text_width > popup_rect.width:

            scrollbar_width = popup_rect.width
            scrollbar_rect = pygame.Rect(
                popup_rect.left,
                popup_rect.bottom - SCROLLBAR_HEIGHT,
                scrollbar_width,
                SCROLLBAR_HEIGHT
            )

            pygame.draw.rect(screen, SCROLLBAR_COLOR, scrollbar_rect)

            thumb_width = popup_rect.width * (popup_rect.width / text_width)
            thumb_rect = pygame.Rect(
                popup_rect.left,
                popup_rect.bottom - SCROLLBAR_HEIGHT,
                thumb_width,
                SCROLLBAR_HEIGHT
            )

            pygame.draw.rect(screen, (150, 150, 150), thumb_rect)

            text_offset_x = -int((text_width - popup_rect.width) * (thumb_rect.left - popup_rect.left) / (popup_rect.width - thumb_width))
        else:
            text_offset_x = 0

        pygame.draw.rect(screen, POPUP_COLOR, popup_rect)

        screen.blit(text_surface, (popup_rect.left + text_offset_x, popup_rect.top + 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.update()