from settings import *
# Block Class
class Block(pygame.sprite.Sprite):
    # properties init func
    def __init__(self, group, pos, color)->None:
        # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)
        
        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)
        
    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE