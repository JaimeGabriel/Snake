import pygame

# Program window dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Game window dimensions
GAME_WIDTH = int(SCREEN_WIDTH * 45/100)
GAME_HEIGHT = int(SCREEN_HEIGHT * 90/100)

# Game size
COLUMNS = 20 # Number of horizontal cells in the game
ROWS = COLUMNS * GAME_HEIGHT // GAME_WIDTH
CELLSIZE = GAME_WIDTH // COLUMNS

# Score window dimensions
SCORE_SCREEN_WIDTH = int(SCREEN_WIDTH * 45/100)
SCORE_SCREEN_HEIGHT = int(SCREEN_HEIGHT * 45/100)

# Blank spaces
BLANK_HORIZONTAL_SPACE = int(SCREEN_WIDTH * 3.3/100)
BLANK_VERTICAL_SPACE = int(SCREEN_WIDTH * 3.3/100)
PIXELS_LINE_BREAK = 15

# Game window origin coordinates
game_x = int(SCREEN_WIDTH * 3.3/100)
game_y = int(SCREEN_HEIGHT * 3.3/100)


# Game speed
HZ_GAME = 60
HZ_FPS_RATIO = 4
FPS = HZ_GAME//HZ_FPS_RATIO


# Colors used in the game
COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 100),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'TRANSPARENT': (0, 0, 0)
}

# ASCII Art
ASCII_ART = """  _____ ____    ____  __  _    ___ 
 / ___/|    \  /    ||  |/ ]  /  _]
(   \_ |  _  ||  o  ||  ' /  /  [_ 
 \__  ||  |  ||     ||    \ |    _]
 /  \ ||  |  ||  _  ||     ||   [_ 
 \    ||  |  ||  |  ||  .  ||     |
  \___||__|__||__|__||__|\_||_____|                                  

"""

