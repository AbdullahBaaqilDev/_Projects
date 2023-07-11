import pygame
import sys
from board import *
from settings import *

class Chess():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Chess")
        pygame.display.set_icon(WINDOW_ICON)
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.board.load_fen(START_FEN)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(BG_COLOR)

            self.board.update()

            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == "__main__":
    chess = Chess()
    chess.mainloop()