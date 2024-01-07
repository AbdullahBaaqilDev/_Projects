from pygame.math import Vector2 as Vec
support_path = __file__
project_path_list = support_path.split("\\")[:-2]
for index in range(1, len(project_path_list) * 2, 2):
    project_path_list.insert(index, "\\")
PROJECT_FOLDER = "".join(project_path_list)


FPS = 120

# sizes
SQUARE_SIZE = 40
BOARD_SIZE = Vec(15,15)
WIDTH = BOARD_SIZE.x * SQUARE_SIZE
HEIGHT = BOARD_SIZE.y * SQUARE_SIZE

# colors
DARK = (61,217,61)
LIGHT = (120,242,102)
UI_FONT_COLOR = (20,20,20)

# snake settings
SNAKE_START_BODY = [Vec(1,12),Vec(2,12),Vec(3,12)]
SNAKE_MOVE_COOLDOWN = 150

# fruits
FRUITS_NUMBER = 3
FRUIT_TYPE = "apple"
FRUITS_LIST = ["apple","watermelon","orange","lemon","cherry","banana","strawberry","avocado","tomato"]
