from pygame.math import Vector2 as Vec
path = __file__.split("\\")
del(path[-2:])
path_as_str = ""
for f in path:
    path_as_str += f+"\\"
PROJECT_FOLDER = path_as_str

FPS = 120

# sizes
SQUARE_SIZE = 40
BOARD_SIZE = Vec(15,15)
WIDTH = BOARD_SIZE.x * SQUARE_SIZE
HEIGHT = BOARD_SIZE.y * SQUARE_SIZE

# colors
DARK = (36,199,36)
LIGHT = (120,242,102)
UI_FONT_COLOR = (20,20,20)

# snake settings
SNAKE_START_BODY = [Vec(1,12),Vec(2,12),Vec(3,12)]
SNAKE_SPEED = 150

# fruits
FRUITS_NUMBER = 7
FRUIT_TYPE = "tomato"
FRUITS_DICT = {
    "apple": 0,
    "watermelon": 1,
    "orange": 2,
    "lemon": 3,
    "cherry": 4,
    "banana": 5,
    "strawberry": 6,
    "avocado": 7,
    "tomato": 8,
}