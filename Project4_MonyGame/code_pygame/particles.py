import pygame
from settings import *
from support import *

class ParticlesAnimationPlayer():
    def __init__(self):
        self.animations = {
            "money":[
                import_folder(f"{PROJECT_FOLDER}\\assets\\particles\\money"),
                self.reflect_images(import_folder(f"{PROJECT_FOLDER}\\assets\\particles\\money"))
                ]
        }

    def reflect_images(frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_particle(self,animation,pos,groups):
        animation_frames = self.animations[animation]
        Particle(pos,animation_frames,groups)
                
class Particle(pygame.sprite.Sprite):
    def __init__(self,animation,pos,groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.animation = animation
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = animation[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.kill()

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center = (self.rect.centerx + int(self.frame_index),self.rect.centery))

    def draw(self):
        self.display_surface.blit(self.image,self.rect)

    def update(self):
        self.animate()
        self.draw()