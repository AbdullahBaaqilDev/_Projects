import pygame
from pygame import Vector2 as Vec
from settings import *
from random import choice
from support import *

class Snake():
    def __init__(self, ground, body = SNAKE_START_BODY, color = "blue", move_sounds = {}):
        self.ground = ground
        self.move_sounds = move_sounds

        self.body = [Vec(body_part) for body_part in body]
        self.direction = Vec(0,0)
        self.move_cooldown = SNAKE_MOVE_COOLDOWN
        self.move_time = None
        self.can_move = True
        
        self.eat = False

        self.color = color
        self.loaded_colors = []
        self.import_graphics(color)

    def import_graphics(self,new_color):
        self.color = new_color
        if new_color not in [color["color"] for color in self.loaded_colors]:
            head_images = {
                "u": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\head_u.png"),
                "d": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\head_d.png"),
                "r": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\head_r.png"),
                "l": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\head_l.png"),
                }
            body_images = {
                "tr": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_tr.png"),
                "tl": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_tl.png"),
                "br": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_br.png"),
                "bl": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_bl.png"),
                "h": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_h.png"),
                "v": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\body_v.png"),
            }
            tail_images = {
                "u": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\tail_u.png"),
                "d": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\tail_d.png"),
                "r": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\tail_r.png"),
                "l": pygame.image.load(f"{PROJECT_FOLDER}\\assets\\images\\snake\\{new_color}\\tail_l.png"),
            }
            self.loaded_colors.append({"color": new_color, "head": head_images, "body": body_images, "tail": tail_images})
            self.head_images = head_images
            self.body_images = body_images
            self.tail_images = tail_images
        else:
            for color in self.loaded_colors:
                if color["color"] == new_color:
                    self.head_images = color["head"]
                    self.body_images = color["body"]
                    self.tail_images = color["tail"]
        data = load_data()
        data["snake_color"] = self.color
        dump_data(data)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_move:
            if current_time - self.move_time >= self.move_cooldown:
                self.can_move = True

    def keyboard_inputs(self):
        keys = pygame.key.get_pressed()
        old_direction = self.direction
        body_relation =  Vec(self.body[-1]) - Vec(self.body[-2])
        if keys[pygame.K_w] and body_relation.y != 1:
            self.direction = Vec(0,-1)
        elif keys[pygame.K_s] and body_relation.y != -1:
            self.direction = Vec(0,1)
        elif keys[pygame.K_d] and body_relation.x != -1:
            self.direction = Vec(1,0)
        elif keys[pygame.K_a] and body_relation.x != 1:
            self.direction = Vec(-1,0)
        if old_direction != self.direction: choice(self.move_sounds).play()

    def move(self):
        if self.can_move:
            if not self.eat:
                body_copy = [Vec(body) for body in self.body[1:]]
                body_copy.append(Vec(body_copy[-1].x + self.direction.x,body_copy[-1].y + self.direction.y))
                self.body = body_copy[:]
            else:
                body_copy = [Vec(body) for body in self.body[:]]
                body_copy.append(Vec(body_copy[-1].x + self.direction.x,body_copy[-1].y + self.direction.y))
                self.body = body_copy[:]
                self.eat = False
            self.can_move = False
            self.move_time = pygame.time.get_ticks()

    def hit_border(self):
        for body in self.body:
            body = Vec(body)
            # x
            if body.x >= BOARD_SIZE[0]: return True
            elif body.x < 0: return True
            
            # y
            if body.y >= BOARD_SIZE[1]: return True
            elif body.y < 0: return True
    
    def hit_body(self):
        for body_part in self.body:
            body_copy = self.body[:]
            body_copy.remove(body_part)
            for body in body_copy:
                if body_part == body:
                    return True

    def draw(self):
        for index,body in enumerate(self.body):
            body = Vec(body)
            image = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE))
            if body == self.body[-1]:
                body_relation =  (body) - Vec(self.body[-2])
                if body_relation == Vec(1,0): image = self.head_images["r"]
                if body_relation == Vec(-1,0): image = self.head_images["l"]
                if body_relation == Vec(0,-1): image = self.head_images["u"]
                if body_relation == Vec(0,1): image = self.head_images["d"]
            elif body == self.body[0]:
                body_relation = (body) - Vec(self.body[1])
                if body_relation == Vec(1,0): image = self.tail_images["r"]
                if body_relation == Vec(-1,0): image = self.tail_images["l"]
                if body_relation == Vec(0,-1): image = self.tail_images["u"]
                if body_relation == Vec(0,1): image = self.tail_images["d"]
            else:
                previous_body = self.body[index - 1] - body
                next_body = self.body[index + 1] - body
                if previous_body.x == next_body.x:
                    image = self.body_images["v"]
                elif previous_body.y == next_body.y:
                    image = self.body_images["h"]
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

            self.ground.blit(image,rect)

    def update(self):
        self.cooldowns()
        self.keyboard_inputs()
        if self.direction != Vec(0,0): self.move()