import pygame, sys
from configs import *

class BlockPuzzle:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Block Puzzle Game")
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

if __name__ == "__main__":
    program = BlockPuzzle()
    program.run()