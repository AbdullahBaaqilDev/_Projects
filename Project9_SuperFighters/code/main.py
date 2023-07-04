import pygame
import sys
from level import *
from settings import *

class SuperFighters():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Super Fighters")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.level.create_map("map1")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.level.menu()
            self.screen.fill((0,0,0))
            
            self.level.update()

            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == "__main__":
    super_fighters = SuperFighters()
    super_fighters.run()