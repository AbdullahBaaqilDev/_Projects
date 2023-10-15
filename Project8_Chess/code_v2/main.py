import pygame, sys
from board import MainBoard
from settings import *

class Chess():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        window_icon = pygame.image.load(WINDOW_ICON)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chess")
        pygame.display.set_icon(window_icon)
        
        self.board = MainBoard(START_FEN)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.board.update()
                
                pygame.display.update()

if __name__ == "__main__":
    programe = Chess()
    programe.run()