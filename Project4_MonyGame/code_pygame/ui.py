import pygame
from settings import *
from button import Button
from upgrades import Upgrades

class UI():
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\font\\joystix.ttf")
        self.player = player
        # upgrades
        self.upgrades = Upgrades(self.player)
        self.upgrades_names = ["Money +","Clicks +","BOOST","Auto Clicker"]
        self.upgrades_costs = [20,30,150,1000]
        self.upgrade_button_width = self.display_surface.get_width() * 0.25
        self.upgrade_button_height = self.display_surface.get_height() * 0.4
        self.create__buttons()

    def create__buttons(self):
        self.buttons_list = []

        for index,button in enumerate(self.upgrades_names):
            full_width = self.display_surface.get_width()
            increment = full_width // len(self.upgrades_names)
            left = (index * increment) + (increment - self.upgrade_button_width) // 2

            top = self.display_surface.get_height() * 0.6

            # create the object
            button = Button(
                text = button,
                cost = self.upgrades_costs[index],
                pos = (left,top),
                size = (self.upgrade_button_width,self.upgrade_button_height),
                command = self.upgrades.upgrades_commands[index],
                press_cooldown = 200,
                index = index,
                font = self.font)
            self.buttons_list.append(button)
        
        money_button = Button(
            text = "Get Money",
            cost = 0,
            pos = (0,200),
            size = (200,100),
            command = self.player.add_money,
            press_cooldown = 500,
            index = index,
            font = self.font)
        self.buttons_list.append(money_button)
    
    def diplay_money_clicks(self):
        surf = self.font.render(f"Money: {self.player.money}",False,MONEY_COLOR)
        self.display_surface.blit(surf,(0,0))

        surf = self.font.render(f"Clicks: {self.player.clicks}",False,CLICKS_COLOR)
        self.display_surface.blit(surf,(0,20))

    def display_upgrads(self):
        pass

    def display_buttons(self):
        for button in self.buttons_list:
            button.update()

    def display(self):
        self.diplay_money_clicks()
        self.display_upgrads()
        self.display_buttons()