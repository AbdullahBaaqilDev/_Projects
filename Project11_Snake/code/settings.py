file_path = __file__
project_path_list = file_path.split("\\")[:-2]
for index in range(1, len(project_path_list) * 2 - 1, 2):
    project_path_list.insert(index, "\\")
PROJECT_FOLDER = "".join(project_path_list)


FPS = 120

# sizes
SQUARE_SIZE = 40
BOARD_SIZE = (12,12)# max 15x15        min 4x6


# colors
DARK = (61,217,61)
VERY_DARK = (38,140,38)
LIGHT = (120,242,102)
UI_FONT_COLOR = (243,244,231)

# snake settings
SNAKE_START_BODY = [(1,5),(2,5),(3,5)]
SNAKE_MOVE_COOLDOWN = 150

# ui counters
COUNTERS_CONFIGS = {
    "fruits_eaten_counter": {"min": 0, "max": None, "pos": (95,20), "in_settings": False, "justfiy": "topleft", "font": "font20"},
    "highest_score_counter": {"min": 0, "max": None, "pos": (220,20), "in_settings": False, "justfiy": "topleft", "font": "font20"},
    "wins_counter": {"min": 0, "max": None, "pos": (345,20), "in_settings": False, "justfiy": "topleft", "font": "font20"},
    "fruits_on_board_counter": {"min": 0, "max": 20, "pos": (135,255), "in_settings": True, "justfiy": "center", "font": "font40"},
}

# ui buttons
BUTTONS_CONFIGS = {
    "resume": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\actv.png"},"text": "Resume","pos": (40,380),"justfiy": "topleft","allow_hold": False},
    "reset_highest_score": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\actv.png"},"text": "Rest Score","pos": (40,315),"justfiy": "topleft","allow_hold": False},

    "increase_volume": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\actv.png"},"text": "","pos": (230,130),"justfiy": "center","allow_hold": True},
    "decrease_volume": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\actv.png"},"text": "","pos": (25,130),"justfiy": "center","allow_hold": True},

    "increase_fruits": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\actv.png"},"text": "","pos": (230,260),"justfiy": "center","allow_hold": False},
    "decrease_fruits": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\actv.png"},"text": "","pos": (25,260),"justfiy": "center","allow_hold": False},

    "snake_color_blue": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\blue\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\blue\\actv.png"},"text": "","pos": (365,80),"justfiy": "topleft","allow_hold": False},
    "snake_color_red": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\red\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\red\\actv.png"},"text": "","pos": (365,120),"justfiy": "topleft","allow_hold": False},
    "snake_color_yellow": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\yellow\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\yellow\\actv.png"},"text": "","pos": (365,160),"justfiy": "topleft","allow_hold": False},
    "snake_color_pink": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\pink\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\pink\\actv.png"},"text": "","pos": (365,200),"justfiy": "topleft","allow_hold": False},
    "snake_color_purple": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\purple\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\purple\\actv.png"},"text": "","pos": (455,80),"justfiy": "topleft","allow_hold": False},
    "snake_color_black": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\black\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\black\\actv.png"},"text": "","pos": (455,120),"justfiy": "topleft","allow_hold": False},
    "snake_color_gray": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\gray\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\gray\\actv.png"},"text": "","pos": (455,160),"justfiy": "topleft","allow_hold": False},
    "snake_color_white": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\white\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\snake_colors\\white\\actv.png"},"text": "","pos": (455,200),"justfiy": "topleft","allow_hold": False},

    "friute_type_apple": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\apple\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\apple\\actv.png"},"text": "","pos": (335,300),"justfiy": "topleft","allow_hold": False},
    "friute_type_watermelon": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\watermelon\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\watermelon\\actv.png"},"text": "","pos": (335,360),"justfiy": "topleft","allow_hold": False},
    "friute_type_orange": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\orange\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\orange\\actv.png"},"text": "","pos": (395,300),"justfiy": "topleft","allow_hold": False},
    "friute_type_cherry": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\cherry\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\cherry\\actv.png"},"text": "","pos": (395,360),"justfiy": "topleft","allow_hold": False},
    "friute_type_banana": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\banana\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\banana\\actv.png"},"text": "","pos": (455,300),"justfiy": "topleft","allow_hold": False},
    "friute_type_strawberry": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\strawberry\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\strawberry\\actv.png"},"text": "","pos": (455,360),"justfiy": "topleft","allow_hold": False},
    "friute_type_avocado": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\avocado\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\avocado\\actv.png"},"text": "","pos": (515,300),"justfiy": "topleft","allow_hold": False},
    "friute_type_tomato": {"images": {"normal": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\tomato\\normal.png","actv": f"{PROJECT_FOLDER}\\assets\\images\\ui\\fruits_types\\tomato\\actv.png"},"text": "","pos": (515,360),"justfiy": "topleft","allow_hold": False},
}

# ui images
settings_menu = {"pos": ((BOARD_SIZE[0] * SQUARE_SIZE) // 2 + 60,(BOARD_SIZE[1] * SQUARE_SIZE) // 2 + 90), "justfiy": "center"}

IMAGES_POS = {
    "apple": {"image":f"{PROJECT_FOLDER}\\assets\\images\\ui\\apple.png","pos": (50, 20), "justfiy": "topleft"},
    "highest_score_trophy": {"image":f"{PROJECT_FOLDER}\\assets\\images\\ui\\highest_score_trophy.png","pos": (175, 20), "justfiy": "topleft"},
    "win_medal": {"image":f"{PROJECT_FOLDER}\\assets\\images\\ui\\win_medal.png","pos": (300, 20), "justfiy": "topleft"},
}

# ui texts
TEXTS_POS = {
    "Volume": {"pos": (25,70), "justfiy": "topleft"},
    "Fruits Number": {"pos": (25,175), "justfiy": "topleft"},
    "Snake Color": {"pos": (375,25), "justfiy": "topleft"},
    "Fruit Type": {"pos": (380,245), "justfiy": "topleft"},
}