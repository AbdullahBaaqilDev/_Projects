import pygame
from pygame import Vector2 as Vec
from debug import debug
from settings import *

class Snake():
    def __init__(self,body: list = SNAKE_START_BODY):
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.move_sound = pygame.mixer.Sound(f"{PROJECT_FOLDER}\\assets\\sounds\\move.wav")
        self.move_sound.set_volume(0.4)
        self.body: list(Vec,...) = body
        self.direction: Vec = Vec(0,0)
        self.speed: int = SNAKE_SPEED
        self.eat: bool = False
        self.move_cooldown: int = SNAKE_SPEED
        self.move_time = None
        self.can_move: bool = True
        self.import_graphics()

    def import_graphics(self):
        self.head_images = {
            "u": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\head_u.png"),
            "d": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\head_d.png"),
            "r": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\head_r.png"),
            "l": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\head_l.png"),
            }
        self.body_images = {
            "tr": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_tr.png"),
            "tl": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_tl.png"),
            "br": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_br.png"),
            "bl": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_bl.png"),
            "h": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_h.png"),
            "v": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\body_v.png"),
        }
        self.tail_images = {
            "u": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\tail_u.png"),
            "d": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\tail_d.png"),
            "r": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\tail_r.png"),
            "l": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\tail_l.png"),
        }

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_move:
            if current_time - self.move_time >= self.move_cooldown:
                self.can_move = True

    def keyboard_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.direction.y != 1:
            if self.direction.y == 0: self.move_sound.play()
            self.direction = Vec(0,-1)
        elif keys[pygame.K_s] and self.direction.y != -1:
            if self.direction.y == 0: self.move_sound.play()
            self.direction = Vec(0,1)
        elif keys[pygame.K_d] and self.direction.x != -1:
            if self.direction.x == 0: self.move_sound.play()
            self.direction = Vec(1,0)
        elif keys[pygame.K_a] and self.direction.x != 1:
            if self.direction.x == 0: self.move_sound.play()
            self.direction = Vec(-1,0)

    def move(self):
        if self.can_move:
            if not self.eat:
                body_copy = self.body[1:]
                body_copy.append(Vec(body_copy[-1].x + self.direction.x,body_copy[-1].y + self.direction.y))
                self.body = body_copy[:]
            else:
                body_copy = self.body[:]
                body_copy.append(Vec(body_copy[-1].x + self.direction.x,body_copy[-1].y + self.direction.y))
                self.body = body_copy[:]
                self.eat = False
            self.can_move = False
            self.move_time = pygame.time.get_ticks()

    def check_border(self):
        for body in self.body:
            # x
            if body.x >= BOARD_SIZE.x: return True
            elif body.x < 0: return True
            
            # y
            if body.y >= BOARD_SIZE.y: return True
            elif body.y < 0: return True
    
    def ckeck_body(self):
        for main_body in self.body:
            body_copy = self.body[:]
            body_copy.remove(main_body)
            for second_body in body_copy:
                if main_body == second_body:
                    return True

    def draw(self):
        for index,body in enumerate(self.body):
            image = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
            image.fill((255,0,0))
            # head
            if body == self.body[-1]:
                body_relation =  body - self.body[-2]
                if body_relation == Vec(1,0): image = self.head_images["r"]
                if body_relation == Vec(-1,0): image = self.head_images["l"]
                if body_relation == Vec(0,-1): image = self.head_images["u"]
                if body_relation == Vec(0,1): image = self.head_images["d"]
            # tail
            elif body == self.body[0]:
                body_relation = body - self.body[1]
                if body_relation == Vec(1,0): image = self.tail_images["r"]
                if body_relation == Vec(-1,0): image = self.tail_images["l"]
                if body_relation == Vec(0,-1): image = self.tail_images["u"]
                if body_relation == Vec(0,1): image = self.tail_images["d"]
            else:
                previous_body = self.body[index - 1] - body
                next_body = self.body[index + 1] - body
                # body
                if previous_body.x == next_body.x:
                    image = self.body_images["v"]
                elif previous_body.y == next_body.y:
                    image = self.body_images["h"]
                # cornur
                else:
                    if previous_body.x == -1 and next_body.y == -1 or\
                       previous_body.y == -1 and next_body.x == -1:
                        image = self.body_images["tl"]
                    elif previous_body.y == -1 and next_body.x == 1 or\
                         previous_body.x == 1 and next_body.y == -1:
                        image = self.body_images["tr"]
                    elif previous_body.x == -1 and next_body.y == 1 or\
                         previous_body.y == 1 and next_body.x == -1:
                        image = self.body_images["bl"]
                    else:
                        image = self.body_images["br"]
            rect = pygame.Rect(body.x * SQUARE_SIZE, body.y * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
            
            self.display_surface.blit(image,rect)

    def update(self):
        self.cooldowns()
        self.keyboard_inputs()
        if self.direction != Vec(0,0): self.move()
        self.draw()