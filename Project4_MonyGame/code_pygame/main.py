import pygame, sys
from ui import UI
from settings import *

class Player():
    def __init__(self,money,clicks):
        self.money = money
        self.clicks = clicks
        self.money_add = 1
        self.clicks_add = 1
    
    def add_money(self):
        self.money += self.money_add
        self.clicks += self.clicks_add

class Main():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Money Game")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(9999999,999)
        self.ui = UI(self.player)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(SCREEN_COLOR)

            self.ui.display()
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Main()
    game.mainloop()