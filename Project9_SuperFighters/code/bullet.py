import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,gun_type):
        super().__init__()
        self.direction = direction
        self.images = []
        self.gun_type = gun_type
        self.spread = random.randint(-arms_dect[self.gun_type][3],arms_dect[self.gun_type][3])
        for index in range(len(os.listdir(f"{assets_path}\\arms\\bullets\\{gun_type}_bullet"))):
            if self.gun_type == "flamethrower":
                if index > 9:
                    break
                img = pygame.image.load(f"{assets_path}\\arms\\bullets\\{gun_type}_bullet\\{random.randint(0,1)}{index}.png")
                img = pygame.transform.scale_by(img,(random.randint(1,10))/10)
            else:
                img = pygame.image.load(f"{assets_path}\\arms\\bullets\\{gun_type}_bullet\\{index}.png")
            if self.gun_type == "lasergun":
                img = pygame.transform.scale(img,(50,img.get_height()))
                self.spread = 0

            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(center = (x+(self.width*self.direction),y+self.spread))
        self.damage = arms_dect[gun_type][0]
        self.speed = arms_dect[gun_type][1]
        if self.direction == 1:
            self.hit_range = pygame.rect.Rect(self.rect.left,y+random.randint(-5,5),self.width,self.height)
            self.flip = True
        if self.direction == -1:
            self.hit_range = pygame.rect.Rect(self.rect.left,y+random.randint(-5,5) ,self.width,self.height)
            self.flip = False

    
    def update(self):
        self.dx,self.dy = 0,0 

        self.dx += self.speed*self.direction
        self.hit_range.x += self.speed*self.direction

        if self.frame_index < len(self.images)-1:
            self.frame_index += 1
            if self.gun_type == "flamethrower":
                self.frame_index -= 0.3
        else:
            self.frame_index = 0
            if self.gun_type == "flamethrower":
                self.kill()
        self.image = self.images[int(self.frame_index)]

        for tile in world.tile_list:
            #check collision with walls
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.kill()
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                self.kill()

        
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x >= SCREEN_WIDTH:
            self.kill()
        if self.rect.x <= 0:
            self.kill()

        
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)    