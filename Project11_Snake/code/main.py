import pygame
import sys
from settings import *
from board import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Board()

    def mianloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(DARK)

            self.level.update()

            self.clock.tick(FPS)
            pygame.display.update()
if __name__ == "__main__":
    runner = Game()
    runner.mianloop()