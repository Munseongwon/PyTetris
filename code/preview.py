from settings import *
# Preview Class
class Preview:
    # properties init func
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
    # draw Preview func
    def run(self) -> None:
        self.display_surface.blit(self.surface, self.rect)
        