import pygame
from player import *
from tile import *
from support import *
from settings import *

class Level():
    def __init__(self,):
        self.display_surf = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.players_group = pygame.sprite.Group()

        self.bullets_group = pygame.sprite.Group()
        self.grenades_group = pygame.sprite.Group()
        self.explosions_group = pygame.sprite.Group()
        self.barrels_group = pygame.sprite.Group()
        self.boxes_group = pygame.sprite.Group()
        self.doors_group = pygame.sprite.Group()

        self.player1 = Player(300,400,"agent",0,[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites)
        self.player2 = Player(400,400,"agent",1,[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites)
        self.players_group.add(self.player1,self.player2)

    def create_map(self,map):
        tile_map = {
            "object": import_csv_layout(f"{PROJECT_FOLDER}\\maps\\{map}\\objects.csv"),
            "block": import_csv_layout(f"{PROJECT_FOLDER}\\maps\\{map}\\blocks.csv"),
            "entity": import_csv_layout(f"{PROJECT_FOLDER}\\maps\\{map}\\entities.csv")
        }
        graphics = {
            "blocks": import_folder(f"{PROJECT_FOLDER}\\assets\\blocks"),
        }

        for style,layout in tile_map.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE

                        if style == "boundary":
                            Tile((x,y),[self.obstacle_sprites])
                        elif style == "block":
                            surface = graphics["blocks"][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],surface)
                        elif style == "entities":
                            if col == "0":
                                self.player1 = Player(
                                    (x,y),
                                    [self.visible_sprites,self.obstacle_sprites],
                                    self.obstacle_sprites,
                                    )
                            else:
                                self.player2 = Player(
                                    (x,y),
                                    [self.visible_sprites,self.obstacle_sprites],
                                    self.obstacle_sprites,
                                    )

    def draw(self):
        for tile in self.tile_list:
            self.display_surf.blit(tile[0], tile[1])
    
    def update(self):
        return