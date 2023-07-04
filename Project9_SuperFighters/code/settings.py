PROJECT_FOLDER = "D:\\Abdullah\\PROGRAMS\\Coding\\_PYTHON\\_Projects\\Project9_SuperFighters"
FPS = 60
WIDTH = 960
HEIGHT = 640
TILE_SIZE = 16

# players
GRAVITY = 0.60
PLAYERS_STATS = {
    "health":1000,
    "max_health":1000,
    "speed":6,
    "jump_space":-8,
    "weapons":{
        "melee_weapon":["punch",None],
        "range_weapon":["pistol",30],
        "bomb_weapon":["gernade",3]
    },
}

# data
MELEE_WEAPONS = {
    "axe":{"damage":30,"hit_speed":FPS},
    "katana":{"damage":30,"hit_speed":FPS},
    "knighf":{"damage":30,"hit_speed":FPS},
    "thick_sowrd":{"damage":30,"hit_speed":FPS},
}

RANGE_WEAPONS = {
    "pistol":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "assaultrifle":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "flamethrower":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "shotgun":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "RBG":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "deathmachine":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "advanced_deathmachine":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "raygun":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "laser_rifle":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "laser_pistol":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
    "laser_shotgun":{"damage":20,"speed":20,"shoot_speed":10,"spreed":2,"automatic":False},
}
# colors
BLACK = (0,0,0)
RED = (227,45,61)
BLACK_UI_COLOR = (0,0,0)
WHITE_UI_COLOR = (255,255,255)
# ui
UI_OFFSET_X = 10
UI_OFFSET_Y = 5
UI_BAR_OFFSET_X = 42
UI_BAR_OFFSET_Y = 10
BAR_WIDTH = 100
BAR_HEIGHT = 25