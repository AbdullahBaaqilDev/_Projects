import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.images = []
        for i in range(len(os.listdir(f"{assets_path}\\arms\explosion"))):
            img = pygame.image.load(f'{assets_path}\\arms\explosion\{i}.png').convert_alpha()
            img = pygame.transform.scale_by(img,scale)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
    


    def update(self):

        EXPLOSION_SPEED = 4
        #update explosion amimation
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            #if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]
        
        # draw
        self.frame_index +=1