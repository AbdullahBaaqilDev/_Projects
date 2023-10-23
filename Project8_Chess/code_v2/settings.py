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
PIECES_IMAGES = {
    "K": f"{ASSETS_FOLDER}\\images\\white\\king.png",
    "k": f"{ASSETS_FOLDER}\\images\\black\\king.png",
    "Q": f"{ASSETS_FOLDER}\\images\\white\\qween.png",
    "q": f"{ASSETS_FOLDER}\\images\\black\\qween.png",
    "B": f"{ASSETS_FOLDER}\\images\\white\\bishop.png",
    "b": f"{ASSETS_FOLDER}\\images\\black\\bishop.png",
    "N": f"{ASSETS_FOLDER}\\images\\white\\knight.png",
    "n": f"{ASSETS_FOLDER}\\images\\black\\knight.png",
    "R": f"{ASSETS_FOLDER}\\images\\white\\rook.png",
    "r": f"{ASSETS_FOLDER}\\images\\black\\rook.png",
    "P": f"{ASSETS_FOLDER}\\images\\white\\pawn.png",
    "p": f"{ASSETS_FOLDER}\\images\\black\\pawn.png",
}
START_FEN = "rnbqkbnr/pppppppp/////PPPPPPPP/RNBQKBNR w KQkq 1000-1000"

LONG_PIECES_DIRECTIONS = {
    "q": [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)],
    "r": [(0, -1), (1, 0), (0, 1), (-1, 0)],
    "b": [(-1, -1), (1, -1), (1, 1), (-1, 1)],
}

SHORT_PIECES_MOVES = {
    "k": [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (2, 0), (-2, 0)],
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
DARK         = (171, 122, 101)
LIGHT        = (238, 216, 192)
DARK_RED     = (197, 68, 79)
LIGHT_RED    = (214, 86, 86)
DARK_YELLOW  = (207,178,66)
LIGHT_YELLOW = (221, 208, 124)

SQUARE_COLORS = {
    True: {"normal": LIGHT, "red": LIGHT_RED, "yellow": LIGHT_YELLOW},
    False : {"normal": DARK, "red": DARK_RED, "yellow": DARK_YELLOW},
}