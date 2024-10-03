from settings import *
from Block import *

class Tetromino:
    # properties init func
    def __init__(self, shape, group, create_new_tetromino, field_data) -> None:
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
        self.create_new_tetromino = create_new_tetromino
        self.field_data = field_data
        
        # create block
        self.blocks = [Block(group, pos, self.block_color) for pos in self.block_positions]
    
    # collisions
    def next_move_horizontal_collide(self, blocks, amount):
        collision_list = [block.horiznotal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False
    
    # movement
    def move_horizontal(self, amount)->None:
        if not self.next_move_horizontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount
    
    def move_down(self)->None:
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()
        