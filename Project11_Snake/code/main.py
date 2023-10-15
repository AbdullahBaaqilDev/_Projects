import pygame, sys
from board import Board
from settings import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.board = Board()
 
    def mianloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.board.menu = not self.board.menu

            self.screen.fill((0,0,0))

            self.board.update()

            self.clock.tick(FPS)
            pygame.display.update()

if __name__ == "__main__":
    runner = Game()
    runner.mianloop()