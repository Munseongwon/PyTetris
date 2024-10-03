from settings import *
from tetromino import *
from random import choice
from gtimer import Timer

# Game Class
class Game:
    # properties init func
    def __init__(self) -> None:
        # general
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        
        # lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(120)
        
        # tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOES.keys())), self.sprites)
        
        # timer
        self.timers = {
            'vertical move':Timer(UPDATE_START_SPEED, True, self.move_down)
        }
        self.timers['vertical move'].activate()
    
    # timer update
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()
    
    # vertical block movement
    def move_down(self):
        self.tetromino.move_down()
    
    # draw grid
    def draw_grid(self) -> None:
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1)    
        
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0, y), (self.surface.get_width(), y), 1)
    
        self.surface.blit(self.line_surface, (0, 0))
        
    # draw Game Screen Surface
    def run(self) -> None:
        # update
        self.timer_update()
        self.sprites.update()
        
        # drawing
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface)
        
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

