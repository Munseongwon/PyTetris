from settings import *
# Score Class
class Score:
    # properties init func
    def __init__(self) -> None:
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()
    
    # draw Score panel func
    def run(self) -> None:
        self.display_surface.blit(self.surface, self.rect)