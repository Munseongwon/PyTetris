from settings import *
# Game Class
class Game:
    # properties init func
    def __init__(self) -> None:
        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
    
    # draw Game Screen Surface
    def run(self) -> None:
        self.display_surface.blit(self.surface, (PADDING, PADDING))
