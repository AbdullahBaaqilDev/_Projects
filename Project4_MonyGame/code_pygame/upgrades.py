import pygame
from button import Button
from settings import *

class Upgrades():
    def __init__(self,parent,player,font):
        self.display_surface = pygame.display.get_surface()
        self.parent = parent
        self.player = player
        self.buttons_group = self.parent.upgrades_buttons
        self.other_buttons = self.parent.buttons
        self.upgrades_commands = [self.upgrade1_command,self.upgrade2_command,self.upgrade3_command,self.upgrade4_command,]
        self.font = font
    
    def boost_command(self):
        self.parent.boosting = True
        self.parent.boosting_start_time = pygame.time.get_ticks()


    def upgrade1_command(self,cost):
        if self.player.money >= cost:
            self.player.money -= cost
            self.player.money_add *= 1.4
            return True
        return False
    
    def upgrade2_command(self,cost):
        if self.player.money >= cost:
            self.player.money -= cost
            self.player.wallets = True
            if self.player.wallets_cooldown > 1000: self.player.wallets_cooldown -= 5
            return True
        return False

    def upgrade3_command(self,cost):
        if self.player.money >= cost:
            if not self.player.boost_active:
                self.boost_button = Button(
                    press_cooldown = self.player.boost_cooldown,
                    text = "Boost",
                    cost = 0,
                    bg = BOOST_UI_BG_COLOR,
                    bg_actv = BOOST_UI_BG_COLOR_SELECTED,
                    fg = BOOST_TEXT_COLOR,
                    fg_actv = BOOST_TEXT_COLOR_SELECTED,
                    border_width = BOOST_BORDER_WIDTH,
                    border_color = BOOST_UI_BORDER_COLOR,
                    border_color_actv = BOOST_UI_BORDER_COLOR_SELECTED,
                    pos = (600,0),
                    size = (100,40),
                    index = 40,
                    command = self.boost_command,
                    font = self.font)
                self.other_buttons.add(self.boost_button)
            self.player.boost_active = True
            if self.player.boost_cooldown > 2500:
                self.player.money -= cost
                self.player.boost_cooldown *= 0.95
                self.boost_button.press_cooldown = self.player.boost_cooldown
                return True
        return False

    def upgrade4_command(self,cost):
        if self.player.money >= cost:
            if self.player.auto_clicker_speed > 70:
                self.player.money -= cost
                self.player.auto_clicker = True
                self.player.auto_clicker_speed -= 20
                return True
        return False