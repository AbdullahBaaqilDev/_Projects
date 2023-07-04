import pygame

class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,player):
        super().__init__()
        self.timer = 120
        self.direction = direction
        self.player_index = player
        self.vel_y = -10
        self.vel_x = 0
        self.speed = 6
        self.image = pygame.image.load(f"{assets_path}\\arms\\firearms\grenade.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx,dy = 0,0
        
        self.vel_y += GRAVITY
        dx += self.direction * self.speed
        dy += self.vel_y
        
        dx += self.vel_x

        #check for collision with level
        for tile in world.tile_list:
            #check collision with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * (self.speed//2)
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.vel_x += self.speed*2*self.direction
                self.speed = 0
                #check if below the ground, i.e. thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom	

        if self.vel_x < 0:
            self.vel_x += 1
        if self.vel_x > 0:
            self.vel_x -= 1

        #update grenade position
        self.rect.x += dx
        self.rect.y += dy

        #countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 3)
            explosion_group.add(explosion)
            #do damage to anyone that is nearby
            if self.player_index == 1:
                if abs(self.rect.centerx - player1.sprite.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player1.sprite.rect.centery) < TILE_SIZE * 2:
                    player1.sprite.health -= 150
            if self.player_index == 0:
                if abs(self.rect.centerx - player2.sprite.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player2.sprite.rect.centery) < TILE_SIZE * 2:
                    player2.sprite.health -= 150