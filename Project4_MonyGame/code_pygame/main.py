import pygame, sys
from ui import UI
from settings import *

class Player():
    def __init__(self,money = 0,clicks = 0):
        self.money = money
        self.money_add = 1
        self.clicks = clicks
        self.clicks_add = 1
        self.wallets = False
        self.wallets_cooldown = WALLET_COOLDOWN

        self.boost_active = False
        self.boost_cooldown = BOOST_COOLDOWN

        self.auto_clicker = False
        self.auto_clicker_speed = AUTO_CLICKER_SPEED
    
    def add_money(self,money_amount,clicks_amount):
        self.money += money_amount
        self.clicks += clicks_amount

class Main():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Money Game")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.ui = UI(self.player)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ui.upgrades_buttons_show = not self.ui.upgrades_buttons_show
            self.screen.fill(SCREEN_COLOR)

            self.ui.update()
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Main()
    game.mainloop()