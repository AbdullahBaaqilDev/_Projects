import pygame
from pygame.math import Vector2 as Vec
from snake import Snake
from fruit import Fruit
from ui import UI
from debug import debug
from support import *
from settings import *

class Board():
    def __init__(self, ground):
        self.display_surface = ground
        self.import_assets()
        data = load_data()

        self.size = Vec(BOARD_SIZE)
        self.square_size = SQUARE_SIZE
        self.squares = set()
        self.create_squares()

        self.snake = Snake(self.display_surface, SNAKE_START_BODY, data["snake_color"], self.move_sounds)
        self.fruits = pygame.sprite.Group()
        self.fruits_type = data["fruits_type"]
        self.fruits_amount = data["fruits_number"]
        for fruit in range(self.fruits_amount): self.create_fruits()
        
        self.score = 0
        self.highest_score = data["highest_score"]
        self.menu = False
        self.ui = UI(self.display_surface, self.ui_assets, data["volume"], self.change_menu, self.change_highest_score, self.snake.import_graphics, self.change_fruits_type, self.change_fruits_number, self.fruits_amount)
        self.volume = self.ui.volume.value

    def change_fruits_type(self, new_type):
        for fruit in self.fruits:
            fruit.change_type(new_type)
        self.fruits_type = new_type
        data = load_data()
        data["fruits_type"] = new_type
        dump_data(data)
    
    def change_fruits_number(self, added):
        old_fruits_number = self.fruits_amount
        self.fruits_amount += added
        if added > 0: self.ui.counters["fruits_on_board_counter"].increase()
        elif added < 0: self.ui.counters["fruits_on_board_counter"].decrease()
        if self.fruits_amount < 0: self.fruits_amount = 0
        elif self.fruits_amount > self.ui.counters["fruits_on_board_counter"].max: self.fruits_amount = self.ui.counters["fruits_on_board_counter"].max
        if self.fruits_amount < old_fruits_number and self.fruits_amount > 0:
            for fruit in range(abs(self.fruits_amount - old_fruits_number)):
                self.fruits.remove(self.fruits.sprites()[-1])
        if self.fruits_amount > old_fruits_number and self.fruits_amount < 20:
            while self.fruits_amount > old_fruits_number:
                self.create_fruits()
                old_fruits_number += 1
        self.change_fruits_type(self.fruits_type)
        data = load_data()
        data["fruits_number"] = self.fruits_amount
        dump_data(data)
    
    def change_highest_score(self, new_score):
        self.highest_score = new_score
        old_data = load_data()
        old_data["highest_score"] = new_score
        dump_data(old_data)
    
    def change_menu(self):
        self.menu = not self.menu
    
    def import_assets(self):
        # sounds
        move_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move.wav")
        move_sound1 = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move1.wav")
        move_sound2 = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move2.wav")
        move_sound3 = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move3.wav")
        move_sound4 = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move4.wav")
        self.move_sounds = [move_sound,move_sound1,move_sound2,move_sound3,move_sound4]
        self.eat_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\eat.wav")
        self.death_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\death.wav")
        self.all_sounds = self.move_sounds + [self.eat_sound, self.death_sound]

        # images
        self.ui_assets = {
            "volume_normal" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\volume\\normal.png"),
            "volume_actv" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\volume\\actv.png"),

            "arrow_right_normal" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\normal.png"),
            "arrow_right_actv" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\right\\actv.png"),
            "arrow_left_normal" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\normal.png"),
            "arrow_left_actv" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\arrow\\left\\actv.png"),

            "button_normal" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\normal.png"),
            "button_actv" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\button\\actv.png"),

            "settings_menu" : pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\ui\\settings_menu.png"),

            # font
            "font20" : pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\fonts\\at01.ttf", 50),
            "font40" : pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\fonts\\at01.ttf", 100),
        }
    
    def get_empty_squares(self, current_fruit = None):
        squares_no_snake = [Vec(square) for square in self.squares if square not in self.snake.body]

        fruits_copy = self.fruits.sprites()[:]
        if current_fruit in fruits_copy: fruits_copy.remove(current_fruit)
        squares_fruits = [fruit.pos for fruit in fruits_copy]
        
        empty_squares = [square for square in squares_no_snake if square not in squares_fruits]
        return empty_squares
    
    def get_fruits_squares(self):
        return [fruit.pos for fruit in self.fruits]
    
    def get_snake_squares(self):
        return [Vec(square) for square in self.squares if square not in self.snake.body]

    def create_squares(self):
        for row in range(int(self.size.x)):
            for column in range(int(self.size.y)):
                self.squares.add((row,column))

    def create_fruits(self):
        Fruit(self.fruits_type, self.get_empty_squares(),[self.fruits])

    def collision(self):
        for fruit in self.fruits:
            if fruit.pos in self.snake.body:
                if len(self.snake.body) == len(self.squares):
                    data = load_data()
                    data["win"] += 1
                    dump_data(data)
                    pygame.quit()
                else:
                    fruit.reposition(self.get_empty_squares(fruit))
                    self.score += 1
                    self.snake.eat = True
                    self.eat_sound.play()
                    if self.score > self.highest_score:
                        self.change_highest_score(self.score)

    def check_death(self):
        if self.snake.hit_border() or self.snake.hit_body():
            self.score = 0
            self.snake.direction = Vec(0,0)
            self.snake.body = SNAKE_START_BODY
            self.death_sound.play()
            for fruit in self.fruits.sprites():
                fruit.reposition(self.get_empty_squares())

    def draw_grass(self):
        for row in range(int(self.size.x)):
            for column in range(int(self.size.y)):
                if (row + column) % 2 != 0: color = DARK
                else: color = LIGHT
                rect = pygame.Rect(row * self.square_size,column * self.square_size,self.square_size,self.square_size)
                pygame.draw.rect(self.display_surface,color,rect)

    def draw(self):
        self.draw_grass()
        self.snake.draw()
        self.fruits.draw(self.display_surface)

    def update(self):
        self.draw()

        if self.menu:
            self.ui.display()
        else:
            self.check_death()
            self.collision()
            self.snake.update()
            self.fruits.update()
        self.ui.always_display()
        self.ui.update_counters(fruits_eaten = self.score, fruits_on_board = self.fruits_amount)
        
        for sound in self.all_sounds:
            sound.set_volume(self.ui.volume.value)
        data = load_data()
        data["volume"] = self.ui.volume.value
        dump_data(data)
