import random
import tkinter as tk
tkwin = tk.Tk()
PROJECT_FOLDER = "D:\Abdullah\PROGRAMS\Coding\_PYTHON\_Projects\Project12_Agar.io"

FPS = 60
WIDTH = 1000
HEIGHT = 600

WORLD_MAP = (50,50)
SQUARE_SIZE = 50


PLAYER_STATUS = {
    "body_color":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "border_color":(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "size":15,
    "speed":7,
    }

FOOD_SIZE_RANGE = (1,5)


LIGHT_BG_COLOR = (255,255,255)
DARK_BG_COLOR = (255,255,255)