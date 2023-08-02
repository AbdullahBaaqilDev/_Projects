import pygame
from snake import Snake
from fruit import Fruit
from ui import UI
from debug import debug
from settings import *

class Board():
    def __init__(self):
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.eat_sound: pygame.mixer.Sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\eat.wav")
        self.death_sound: pygame.mixer.Sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\death.wav")
        self.font_20px = pygame.font.SysFont("Arial",20)
        self.font_30px = pygame.font.SysFont("Arial",30,True)

        self.size: Vec = BOARD_SIZE
        self.square_size: int = SQUARE_SIZE
        self.squares: list = []
        self.create_squares()
        self.fruits: pygame.sprite.Group = pygame.sprite.Group()
        self.fruit_type: str = FRUIT_TYPE
        self.create_fruits()
        self.snake: Snake = Snake()
        self.score: int = 0
        self.get_highest_score()
        self.menu: bool = False
        self.ui = UI()
        
    def get_highest_score(self):
        with open(f"{PROJECT_FOLDER}\\data\\highest_score.txt","r") as highest_score_text:
            self.highest_score: int = int(highest_score_text.read())

    def change_highest_score(self):
        self.highest_score: int = self.score
        with open(f"{PROJECT_FOLDER}\\data\\highest_score.txt","w") as highest_score_text:
            highest_score_text.write(str(self.score))

    def create_squares(self):
        for row in range(int(self.size.x)):
            for column in range(int(self.size.y)):
                self.squares.append(Vec(row,column))

    def create_fruits(self):
        for fruit in range(FRUITS_NUMBER):
            Fruit(self.fruit_type,[self.fruits])

    def collision(self):
        for fruit in self.fruits:
            if fruit.pos == self.snake.body[-1]:
                if len(self.snake.body) == len(self.squares):
                    print("as")
                else:
                    var = True
                    while var:
                        for body in self.snake.body:
                            if fruit.pos == body:
                                fruit.reposition()
                            else:
                                var = False
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
            for fruit in self.fruits.sprites():
                fruit.reposition()

    def display_menu(self):
        self.ui.display()

    def draw_grass(self):
        for row in range(int(self.size.x)):
            for column in range(int(self.size.y)):
                if (row + column) % 2 != 0: color: tuple(int,int,int) = DARK
                else: color: tuple(int,int,int) = LIGHT
                rect: pygame.Rect = pygame.Rect(row * self.square_size,column * self.square_size,self.square_size,self.square_size)
                pygame.draw.rect(self.display_surface,color,rect)

    def draw(self):
        self.draw_grass()

    def update(self):
        if not self.menu:
            self.check_death()
            self.collision()
            self.draw()
            self.snake.update()
            self.fruits.update()
            self.ui.display_text(self.font_30px,str(self.highest_score),True,UI_FONT_COLOR,True)
            self.ui.display_text(self.font_30px,str(self.score),True,UI_FONT_COLOR)
        else:
            self.display_menu()