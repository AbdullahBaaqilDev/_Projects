import pygame
import sys
from world import *
from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((tkwin.winfo_screenwidth(),tkwin.winfo_screenheight()))
        pygame.display.set_caption("Agar.io")
        self.clock = pygame.time.Clock()
        self.fullscreen = True
        
        self.world = World()

    def run(self):
        while True:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if eve.key == pygame.K_F11:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = pygame.display.set_mode((tkwin.winfo_screenwidth(),tkwin.winfo_screenheight()),pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
            self.screen.fill(LIGHT_BG_COLOR)

            self.world.update()

            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == "__main__":
    game = Game()
    game.run()