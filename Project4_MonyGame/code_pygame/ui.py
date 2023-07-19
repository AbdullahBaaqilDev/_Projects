import pygame
from random import randint, choice
from settings import *
from particles import Particle
from wallet import Wallet
from button import Button
from upgrades import Upgrades

class UI():
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\font\\joystix.ttf")
        self.player = player
        self.visible_sprites = pygame.sprite.Group()
        self.upgrades_buttons = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.upgrades_buttons_show = False
        self.wallet_ready = True
        self.boosting = False
        self.boosting_start_time = None
        self.boosting_time = BOOST_TIME
        self.auto_clicker_ready = True
        self.auto_clicker_clicked = None
        self.money_sounds = [pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\money1.mp3"),pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\money2.mp3")]
        self.money_sounds[0].set_volume(0.4)
        self.money_sounds[1].set_volume(0.4)
        self.wallet_sounds = [pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\wallet1.mp3"),pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\wallet2.mp3")]
        
        # upgrades
        self.upgrades = Upgrades(self,self.player,self.font)
        self.upgrades_names = ["Money +","Wallets +","BOOST","Auto Clicker"]
        self.upgrades_costs = [20,30,150,1000]
        self.upgrade_button_width = self.display_surface.get_width() * 0.2
        self.upgrade_button_height = self.display_surface.get_height() * 0.6
        self.create_buttons()
        self.import_assets()

    def import_assets(self):
        self.money_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money\\money.png").convert_alpha()
        self.coin_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money\\coin.png").convert_alpha()
        self.cash1_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money\\cash1.png").convert_alpha()
        self.cash2_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money\\cash2.png").convert_alpha()
        self.banknotes_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money\\banknotes.png").convert_alpha()
        self.money_bag_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money_bags\\money_bag.png").convert_alpha()
        self.wallet_image = pygame.image.load(f"{PROJECT_FOLDER}\\assets\\particles\\money_bags\\wallet.png").convert_alpha()

    def money_button_command(self,pos):
        self.player.add_money(self.player.money_add,self.player.clicks_add)
        Particle(
            image = choice([self.money_image,self.coin_image,self.cash1_image,self.cash2_image,self.banknotes_image,]),
            pos = pos,
            groups = self.visible_sprites)
        choice(self.money_sounds).play()

    def create_buttons(self):
        for index,button in enumerate(self.upgrades_names):
            full_width = self.display_surface.get_width()
            increment = full_width // len(self.upgrades_names)
            left = (index * increment) + (increment - self.upgrade_button_width) // 2

            top = self.display_surface.get_height() * 0.2

            # create the object
            button = Button(
                press_cooldown = None,
                text = button,
                cost = self.upgrades_costs[index],
                bg = UI_BG_COLOR,
                bg_actv = UI_BG_COLOR_SELECTED,
                fg = UI_BG_COLOR_SELECTED,
                fg_actv = UI_BG_COLOR,
                border_width = 5,
                border_color = UI_BORDER_COLOR,
                border_color_actv = UI_BORDER_COLOR_SELECTED,
                pos = (left,top),
                size = (self.upgrade_button_width,self.upgrade_button_height),
                index = index,
                command = self.upgrades.upgrades_commands[index],
                font = self.font)
            self.upgrades_buttons.add(button)
        
        money_button = Button(
            press_cooldown = None,
            text = "Get Money",
            cost = 0,
            bg = MONEY_UI_BG_COLOR,
            bg_actv = MONEY_UI_BG_COLOR_SELECTED,
            fg = MONEY_UI_BG_COLOR_SELECTED,
            fg_actv = MONEY_UI_BG_COLOR,
            border_width = MONEY_BORDER_WIDTH,
            border_color = MONEY_UI_BORDER_COLOR,
            border_color_actv = MONEY_UI_BORDER_COLOR_SELECTED,
            pos = (0,self.display_surface.get_height() * 0.1),
            size = (self.display_surface.get_width(),self.display_surface.get_height() * 0.8),
            index = index,
            command = lambda: self.money_button_command(pygame.math.Vector2(pygame.mouse.get_pos()) + pygame.math.Vector2(randint(-20,20),randint(-20,20))),
            font = self.font)
        self.buttons.add(money_button)
    
    def create_wallet(self):
        Wallet(
            image = choice([self.money_bag_image,self.wallet_image]),
            parent = self,
            money = randint(10,30),
            pos = (0,randint(int(HEIGHT * .1),int(HEIGHT * .8))),
            groups = self.visible_sprites)
        

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.boosting:
            if current_time - self.boosting_start_time >= self.boosting_time:
                self.boosting = False

        if not self.auto_clicker_ready:
            if current_time - self.auto_clicker_clicked >= self.player.auto_clicker_speed:
                self.auto_clicker_ready = True

        if not self.wallet_ready:
            if current_time - self.wallet_start >= self.player.wallets_cooldown:
                self.wallet_ready = True



    def diplay_money_clicks(self):
        surf = self.font.render(f"Money: {round(self.player.money,2)}",False,MONEY_COLOR)
        self.display_surface.blit(surf,(0,0))

        surf = self.font.render(f"Clicks: {round(self.player.clicks,0)}",False,CLICKS_COLOR)
        self.display_surface.blit(surf,(0,20))


    def update(self):
        if self.player.wallets and self.wallet_ready: self.create_wallet() ; self.wallet_start = pygame.time.get_ticks() ; self.wallet_ready = False
        if self.boosting: self.player.add_money(self.player.money_add,self.player.clicks_add)
        if self.player.auto_clicker and self.auto_clicker_ready: self.money_button_command((randint(0,WIDTH),randint(int(HEIGHT * .1),int(HEIGHT * .8)))) ; self.auto_clicker_clicked = pygame.time.get_ticks() ; self.auto_clicker_ready = False
        self.cooldowns()
        self.diplay_money_clicks()
        if self.upgrades_buttons_show: self.upgrades_buttons.update()
        else: self.buttons.update()
        self.visible_sprites.update()