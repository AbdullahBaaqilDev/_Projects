import pygame
from support import load_json, PROJECT_PATH

class BlocksMaker:
    def __init__(self, block_id):
        blocks = load_json(PROJECT_PATH)["blocks"]

    def get_image(self):
        return ""