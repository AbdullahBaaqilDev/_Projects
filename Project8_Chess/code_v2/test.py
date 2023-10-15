import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500,500))

list = []
class Square:
    def __init__(self,index,pos):
        self.index = index
        self.image = pygame.Surface((50,50))
        self.image.fill((20,20,20))
        self.rect = self.image.get_rect(topleft = pos * 50)
        self.font: pygame.font.Font = pygame.sysfont.SysFont(None,20)

    def draw(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.font.render(str(self.index),True,(255,255,255)),pygame.math.Vector2(self.rect.topleft) + pygame.math.Vector2(18,18))
        pygame.draw.rect(screen,(255,255,255),self.rect,2)

for rank in range(8):
    for file in range(8):
        square = Square(file * 8 + rank,pygame.math.Vector2(rank, file))
        list.append(square)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for square in list:
            square.draw()
        
        pygame.display.update()