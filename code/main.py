from settings import *
from sys import exit

# components
from game import Game
from score import Score
from preview import Preview

# Game Main Class
class Main:
    # Game properties init methods
    def __init__(self) -> None:
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption('PyTetris')
        
        # components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()
    
    # Game loop func
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
            # display
            self.display_surface.fill(GRAY)
            
            # components
            self.game.run()
            self.score.run()
            self.preview.run()
            
            # updating the game
            pygame.display.update()
            self.clock.tick()
    
    
    
# Game Main Func
if __name__ == '__main__':
    main = Main()
    main.run()