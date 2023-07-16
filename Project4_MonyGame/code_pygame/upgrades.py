import pygame

class Upgrades():
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.upgrades_commands = [self.upgrade1_command,self.upgrade2_command,self.upgrade3_command,self.upgrade4_command,]
    
    def upgrade1_command(self):
        self.player.money_add *= 1.4
    
    def upgrade2_command(self):
        self.player.clicks_add *= 1.4

    def upgrade3_command(self):
        pass

    def upgrade4_command(self):
        pass