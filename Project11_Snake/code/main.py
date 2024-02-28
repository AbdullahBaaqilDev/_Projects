import pygame, sys
from board import Board
from settings import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((BOARD_SIZE[0] * SQUARE_SIZE + 120, BOARD_SIZE[1] * SQUARE_SIZE + 90))
        self.ground_surf = pygame.Surface((BOARD_SIZE[0] * SQUARE_SIZE, BOARD_SIZE[1] * SQUARE_SIZE + 15))
        self.ground_rect = self.ground_surf.get_rect(midbottom = self.screen.get_rect(topleft = (0,0)).midbottom)
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.board = Board(self.ground_surf)
 
    def mianloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.board.menu = not self.board.menu
            self.screen.fill(VERY_DARK)

            self.screen.blit(self.ground_surf, self.ground_rect)
            self.ground_surf.fill(VERY_DARK)
            self.board.update()

            self.clock.tick(FPS)
            pygame.display.update()

if __name__ == "__main__":
    runner = Game()
    runner.mianloop()