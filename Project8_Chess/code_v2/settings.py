def get_path():
    path_list = __file__.split("\\")
    del(path_list[-2:])
    path_list.append("assets")

    path = ""
    for folder in path_list: path += folder + "\\"
    return path

ASSETS_FOLDER = get_path()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_ICON = f"{ASSETS_FOLDER}\\images\\chess.ico"

SQUARE_SIZE = WINDOW_HEIGHT / 8
PIECES_IMAGE = "D:\\Abdullah\\PROGRAMES\\Coding\\_Python\\_Projects\\Project8_Chess\\assets\\images\\pieces.png"
START_FEN = "rnbqkbnr/pppppppp/////PPPPPPPP/RNBQKBNR w KQkq 1000-1000"

LONG_PIECES_DIRECTIONS = {
    "q": [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)],
    "r": [(0, -1), (1, 0), (0, 1), (-1, 0)],
    "b": [(-1, -1), (1, -1), (1, 1), (-1, 1)],
}

SHORT_PIECES_MOVES = {
    "k": [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)],
    "n": [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)],
    "p": [(0, -1), (0, -2), (1, -1), (-1, -1)],
}

# sound
MOVE_SOUND = f"{ASSETS_FOLDER}\\sounds\\move.wav"
CAPTURE_SOUND = f"{ASSETS_FOLDER}\\sounds\\capture.wav"
CHECK_SOUND = f"{ASSETS_FOLDER}\\sounds\\check.wav"
CASTLE_SOUND = f"{ASSETS_FOLDER}\\sounds\\castle.wav"
PROMOTE_SOUND = f"{ASSETS_FOLDER}\\sounds\\promote.wav"

# colors
DARK         = (181, 136, 99)
LIGHT        = (240, 217, 181)
DARK_RED     = (217, 35, 35)
LIGHT_RED    = (255, 61, 61)
DARK_YELLOW  = (200, 178, 31)
LIGHT_YELLOW = (230, 218, 72)

SQUARE_COLORS = {
    True: {"normal": LIGHT, "red": LIGHT_RED, "yellow": LIGHT_YELLOW},
    False : {"normal": DARK, "red": DARK_RED, "yellow": DARK_YELLOW},
}