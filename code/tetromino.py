from settings import *
from Block import *

class Tetromino:
    # properties init func
    def __init__(self, shape, group) -> None:
        '''
        setup
        {
            'T':'PURPLE'
            'O':'YELLOW'
            'J':'BLUE'
            'L':'ORANGE'
            'I':'CYAN'
            'S':'GREEN'
            'Z':'RED'
        }
        '''
        self.block_positions = TETROMINOES[shape]['shape']
        self.block_color = TETROMINOES[shape]['color']
        
        # create block
        self.blocks = [Block(group, pos, self.block_color) for pos in self.block_positions]
    
    def move_horizontal(self, amount)->None:
        for block in self.blocks:
            block.pos.x += amount
    
    def move_down(self)->None:
        for block in self.blocks:
            block.pos.y += 1