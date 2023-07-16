import pygame
from pygame import Vector2 as Vec

path = __file__.split("\\")
del(path[-2:])
path.append("assets")
path_as_str = ""
for f in path:
    path_as_str += f+"\\"
ASSETS_FOLDER = path_as_str
WIDTH = 1000
HEIGHT = 600
FPS = 120
WINDOW_ICON = pygame.image.load(f"{ASSETS_FOLDER}\\images\\chess.ico")

SQUARE_SIZE = HEIGHT / 8
START_FEN = "rnbqkbnr/pppppppp/////PPPPPPPP/RNBQKBNR w KQkq"

PIECES_DIRETIONS = {
    1:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
    2:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
    3:[Vec(1,-1),Vec(-1,-1),Vec(1,1),Vec(-1,1),],
    4:[Vec(-2,1),Vec(-2,-1),Vec(2,1),Vec(2,-1),Vec(1,2),Vec(-1,2),Vec(1,-2),Vec(-1,-2),],
    5:[Vec(1,0),Vec(-1,0),Vec(0,-1),Vec(0,1),],
    6:[Vec(0,-1),Vec(1,-1),Vec(-1,-1)],
    -6:[Vec(0,1),Vec(-1,1),Vec(1,1)],
}

# squares colors
DARK = (181,136,99)
LIGHT = (240,217,181)
DARK_RED = (217,35,35)
LIGHT_RED = (255,61,61)
DARK_YELLOW = (200,178,31)
LIGHT_YELLOW = (230,218,72)

# square color dect
SQUARES_COLORS_DECT = {
    True:[DARK,DARK_RED,DARK_YELLOW],
    False:[LIGHT,LIGHT_RED,LIGHT_YELLOW],
}

# general colors
BG_COLOR = (81,80,76)
BUTTON_COLOR = (65,64,61)
BORDER_COLOR = (47,46,44)

# other colors
BLACK = (0,0,0)