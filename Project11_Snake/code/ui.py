import pygame
from pygame.math import Vector2 as Vec
from support import *
from settings import *

class Widget(pygame.sprite.Sprite):
    def __init__(self, mother_surf, pos, justfiy):
        self.screen = mother_surf
        self.pos = pos
        self.justfiy = justfiy
    
    def create_rect_1image(self, image):
        self.image = image
        match self.justfiy:
            case "topleft":
                rect = image.get_rect(topleft = self.pos)
            case "topright":
                rect = image.get_rect(topright = self.pos)
            case "bottomleft":
                rect = image.get_rect(bottomleft = self.pos)
            case "bottomright":
                rect = image.get_rect(bottomright = self.pos)
            case _:
                rect = image.get_rect(center = self.pos)
        return rect
    
    def create_rect_2images(self, image1, image2):
        match self.justfiy:
            case "topleft":
                rect1 = image1.get_rect(topleft = self.pos)
                rect2 = image2.get_rect(topleft = self.pos)
            case "topright":
                rect1 = image1.get_rect(topright = self.pos)
                rect2 = image2.get_rect(topright = self.pos)
            case "bottomleft":
                rect1 = image1.get_rect(bottomleft = self.pos)
                rect2 = image2.get_rect(bottomleft = self.pos)
            case "bottomright":
                rect1 = image1.get_rect(bottomright = self.pos)
                rect2 = image2.get_rect(bottomright = self.pos)
            case _:
                rect1 = image1.get_rect(center = self.pos)
                rect2 = image2.get_rect(center = self.pos)
        return rect1, rect2
    
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()

class Button(Widget):
    def __init__(self, mother_surf, text, font, images, pos, justfiy, command, allow_hold):
        super().__init__(mother_surf, pos, justfiy)
        self.text = text
        self.font = font
        self.image_actv = images["actv"]
        self.image_normal = images["normal"]
        self.pressed = False
        self.command = command
        self.allow_hold = allow_hold
        self.run_command_time = 0
        self.cooldown = FPS * 0.3
        self.rect_normal, self.rect_actv = self.create_rect_2images(self.image_normal, self.image_actv)

    def is_pressed(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        current_time = pygame.time.get_ticks()

        if mouse_pressed and self.rect_normal.collidepoint(pygame.mouse.get_pos()):
            self.pressed = True

        if self.allow_hold and current_time - self.run_command_time >= self.cooldown and self.pressed:
            self.run_command_time = current_time
            self.command()
        elif self.pressed and not mouse_pressed:
            self.pressed = False
            self.command()

    def draw(self):
        if pygame.mouse.get_pressed()[0] and self.rect_normal.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.image_actv, self.rect_actv)
            text_surf = self.font.render(self.text, False, UI_FONT_COLOR)
            text_rect = text_surf.get_rect(center = self.rect_actv.center)
            self.screen.blit(text_surf, text_rect)
        else:
            self.screen.blit(self.image_normal, self.rect_normal)
            text_surf = self.font.render(self.text, False, UI_FONT_COLOR)
            text_rect = text_surf.get_rect(center = self.rect_normal.center)
            self.screen.blit(text_surf, text_rect)

    def update(self):
        self.is_pressed()
        self.draw()

class Text(Widget):
    def __init__(self, mother_surf, text, font, color, pos, justfiy):
        self.font = font
        self.color = color
        self.mother_surf = mother_surf
        image = self.font.render(text, False, color)
        super().__init__(mother_surf, pos, justfiy)
        self.rect = self.create_rect_1image(image)
    
    def change_text(self, new_text):
        self.__init__(self.mother_surf, new_text, self.font, self.color, self.pos, self.justfiy)

class Image(Widget):
    def __init__(self, mother_surf, image, pos, justfiy):
        super().__init__(mother_surf, pos, justfiy)
        self.rect = self.create_rect_1image(image)

class Volume(Widget):
    def __init__(self, mother_surf, value, points, point_space, images, pos, justfiy):
        super().__init__(mother_surf, pos, justfiy)
        self.value = value
        self.point_space = point_space
        self.points = points
        self.image_normal = images["normal"]
        self.image_actv = images["actv"]
        self.rect_normal, self.rect_actv = self.create_rect_2images(self.image_normal, self.image_actv)

    def increase(self, amount = 0.1):
        if self.value < 1: self.value += amount
        if self.value > 1: self.value = 1

    def decrease(self, amount = 0.1):
        if self.value > 0: self.value -= amount
        if self.value < 0: self.value = 0

    def draw(self):
        current_percentage = (self.value * 100)
        for point in range(self.points):
            if current_percentage < (point + 1) * (100 / self.points):
                self.screen.blit(self.image_normal, (self.rect_normal.x + (self.point_space * point), self.rect_normal.y))
            else: self.screen.blit(self.image_actv, (self.rect_actv.x + (self.point_space * point), self.rect_actv.y))

    def update(self):
        self.draw()

class Counter():
    def __init__(self, mother_surf, in_settings, value, min, max, font, color, pos, justfiy):
        self.in_settings = in_settings
        self.value = value
        self.min = min
        self.max = max
        self.font = font
        self.color = color
        self.pos = pos
        self.justfiy = justfiy
        self.text_display = Text(mother_surf, str(value), font, color, pos, justfiy)
    
    def set_value(self, value):
        self.value = value
        self.text_display.change_text(str(value))

    def increase(self):
        self.value += 1
        if self.max:
            if self.value > self.max: self.value = self.max
        self.text_display.change_text(str(self.value))

    def decrease(self):
        self.value -= 1
        if self.min:
            if self.value < self.min: self.value = self.min
        self.text_display.change_text(str(self.value))

    def update(self):
        self.text_display.update()

class UI():
    def __init__(self, ground, assets, volume, change_menu, change_highest_score, change_snake_color, change_fruit_type, change_fruits_number, fruits_number):
        self.display_surface = pygame.display.get_surface()
        self.ground = ground

        # buttons functions
        self.change_menu = change_menu
        self.reset_highest_score = lambda: change_highest_score(0)
        self.change_snake_color = change_snake_color
        self.change_fruit_type = change_fruit_type
        self.change_fruits_number = change_fruits_number

        self.assets = assets
        self.settings_menu = Image(self.display_surface, self.assets["settings_menu"], settings_menu["pos"], settings_menu["justfiy"])
        self.volume = Volume(self.display_surface, volume, 20, 8, {"normal": self.assets["volume_normal"], "actv": self.assets["volume_actv"]}, (50,130) + Vec(self.settings_menu.rect.topleft), "topleft")
        self.counters_configs = COUNTERS_CONFIGS
        self.buttons_configs = BUTTONS_CONFIGS
        self.images_pos = IMAGES_POS
        self.texts_pos = TEXTS_POS
        self.counters = {}
        self.buttons = set()
        self.images = set()
        self.texts = set()
        self.create_counters()
        self.create_buttons()
        self.create_texts()
        self.create_images()

    def create_counters(self):
        for name, configs in self.counters_configs.items():
            pos = configs["pos"] if not configs["in_settings"] else configs["pos"] + Vec(self.settings_menu.rect.topleft)
            self.counters[name] = Counter(self.display_surface, configs["in_settings"], 0, configs["min"], configs["max"], self.assets[configs["font"]], UI_FONT_COLOR, pos, configs["justfiy"])

    def create_buttons(self):
        buttons_commands = [
            self.change_menu, self.reset_highest_score,

            lambda: self.volume.increase(1 / self.volume.points),
            lambda: self.volume.decrease(1 / self.volume.points),
            
            lambda: self.change_fruits_number(1),
            lambda: self.change_fruits_number(-1),

            lambda: self.change_snake_color("blue"),
            lambda: self.change_snake_color("red"),
            lambda: self.change_snake_color("yellow"),
            lambda: self.change_snake_color("pink"),
            lambda: self.change_snake_color("purple"),
            lambda: self.change_snake_color("black"),
            lambda: self.change_snake_color("gray"),
            lambda: self.change_snake_color("white"),

            lambda: self.change_fruit_type("apple"),
            lambda: self.change_fruit_type("watermelon"),
            lambda: self.change_fruit_type("orange"),
            lambda: self.change_fruit_type("cherry"),
            lambda: self.change_fruit_type("banana"),
            lambda: self.change_fruit_type("strawberry"),
            lambda: self.change_fruit_type("avocado"),
            lambda: self.change_fruit_type("tomato"),
        ]
        for index, button in enumerate(self.buttons_configs.values()):
            image_normal = pygame.image.load(button["images"]["normal"])
            image_actv = pygame.image.load(button["images"]["actv"])
            self.buttons.add(Button(self.display_surface, button["text"], self.assets["font20"], {"normal": image_normal, "actv": image_actv}, Vec(button["pos"]) + Vec(self.settings_menu.rect.topleft), button["justfiy"], buttons_commands[index], button["allow_hold"]))

    def create_texts(self):
        for text, configs in self.texts_pos.items():
            self.texts.add(Text(self.display_surface, text, self.assets["font20"], UI_FONT_COLOR, Vec(configs["pos"]) + Vec(self.settings_menu.rect.topleft), configs["justfiy"]))
    
    def create_images(self):
        for image in self.images_pos.values():
            self.images.add(Image(self.display_surface, pygame.image.load(image["image"]), image["pos"], image["justfiy"]))

    def update_counters(self, **values):
        data = load_data()
        self.counters["wins_counter"].set_value(data["wins"])
        self.counters["highest_score_counter"].set_value(data["highest_score"])
        self.counters["fruits_on_board_counter"].set_value(values.get("fruits_on_board", 404))
        self.counters["fruits_eaten_counter"].set_value(values.get("fruits_eaten", 404))
        for counter in self.counters.values():
            if not counter.in_settings:
                counter.update()

    def display(self):
        self.settings_menu.update()
        self.volume.update()
        for counter in self.counters.values():
            if counter.in_settings:
                counter.update()
        for button in self.buttons: button.update()
        for text in self.texts: text.update()
    
    def always_display(self):
        for image in self.images: image.update()