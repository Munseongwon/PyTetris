import pygame

# Game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE  # 400, 800

# Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# Window(padding: 20, width: 660, height: 840)
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3 # 660
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2 # 840

# Game Behavior
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS//2, -1)

# Block Colors
YELLOW = (241, 230, 13)
RED = (229, 27, 32)
BLUE = (32, 75, 155)
GREEN = (101, 179, 46)
PURPLE = (123, 33, 127)
CYAN = (108, 198, 217)
ORANGE = (240, 126, 19)
GRAY = (28, 28, 28)
LINE_COLOR = (255, 255, 255)

# Block Shapes
TETROMINOES = {
    'T':{'shape':[(0,0), (-1,0), (1,0), (0,-1)], 'color':PURPLE},
    'O':{'shape':[(0,0), (0,-1), (1,0), (1,-1)], 'color':BLUE},
    'J':{'shape':[(0,0), (0,-1), (0,1), (-1,1)], 'color':YELLOW},
    'L':{'shape':[(0,0), (0,-1), (0,1), (1,1)], 'color':ORANGE},
    'I':{'shape':[(0,0), (0,-1), (0,-2), (0,1)], 'color':CYAN},
    'S':{'shape':[(0,0), (-1,0), (0,-1), (1,-1)], 'color':GREEN},
    'Z':{'shape':[(0,0), (1,0), (0,-1), (-1,-1)], 'color':RED},
}

# Score Data
SCORE_DATA = {1:40, 2:100, 3:300, 4:1200}











