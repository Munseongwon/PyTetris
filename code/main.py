from settings import *
from sys import exit

# components
from game import Game
from score import Score
from preview import Preview
from random import choice

# Game Main Class
class Main:
    # Game properties init methods
    def __init__(self) -> None:
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption('PyTetris')
        
        # shapes
        self.next_shapes = [choice(list(TETROMINOES.keys())) for shape in range(3)]
        
        # components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()
    
    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level
    
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOES.keys())))
        return next_shape
    
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
            self.preview.run(self.next_shapes)
            
            # updating the game
            pygame.display.update()
            self.clock.tick()
                
# Game Main Func
if __name__ == '__main__':
    main = Main()
    main.run()