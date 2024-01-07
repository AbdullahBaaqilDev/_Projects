import pygame
from snake import Snake
from fruit import Fruit
from ui import UI
from debug import debug
from settings import *

class Board():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.eat_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\eat.wav")
        self.death_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\death.wav")
        self.font_20px = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\fonts\\Race Sport.ttf",20)
        self.font_30px = pygame.font.Font(f"{PROJECT_FOLDER}\\assets\\fonts\\Race Sport.ttf",25)

        self.size = BOARD_SIZE
        self.square_size = SQUARE_SIZE
        self.squares = []
        self.create_squares()
        self.snake = Snake()
        self.fruits = pygame.sprite.Group()
        self.fruit_type = FRUIT_TYPE
        self.create_fruits()
        self.score = 0
        self.get_highest_score()
        self.menu = False
        self.ui = UI()
        
    def get_highest_score(self):
        with open(f"{PROJECT_FOLDER}\\data\\highest_score.txt","r") as highest_score_text:
            self.highest_score = int(highest_score_text.read())

    def change_highest_score(self):
        self.highest_score = self.score
        with open(f"{PROJECT_FOLDER}\\data\\highest_score.txt","w") as highest_score_text:
            highest_score_text.write(str(self.score))

    def create_squares(self):
        for row in range(int(self.size.x)):
            for column in range(int(self.size.y)):
                self.squares.append(Vec(row,column))

    def create_fruits(self):
        empty_squares = [square for square in self.squares if square not in self.snake.body]
        for fruit in range(FRUITS_NUMBER):
            Fruit(self.fruit_type, empty_squares,[self.fruits])

    def collision(self):
        for fruit in self.fruits:
            if fruit.pos in self.snake.body:
                if len(self.snake.body) == len(self.squares):
                    print("you win")
                    pygame.quit()
                else:
                    empty_squares = [square for square in self.squares if square not in self.snake.body]
                    fruit.reposition(empty_squares)
                    self.score += 1
                    self.snake.eat = True
                    self.eat_sound.play()
                    if self.score > self.highest_score:
                        self.change_highest_score()

    def check_death(self):
        if self.snake.check_border() or self.snake.ckeck_body():
            self.score = 0
            self.snake.direction = Vec(0,0)
            self.snake.body = SNAKE_START_BODY
            self.death_sound.play()
            empty_squares = [square for square in self.squares if square not in self.snake.body]
            for fruit in self.fruits.sprites():
                fruit.reposition(empty_squares)

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
        if not self.menu:
            self.check_death()
            self.collision()
            self.snake.update()
            self.fruits.update()
            self.ui.display_text(self.font_30px,f"Highest Score: {self.highest_score}",True,UI_FONT_COLOR,)
            self.ui.display_text(self.font_30px,f"Score: {self.score}",True,UI_FONT_COLOR,(0,40))
        
        self.draw()
        
        if self.menu:
            self.ui.display()