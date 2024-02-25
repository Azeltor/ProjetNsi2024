import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('Graphisme\Character\Prototype_Worksheet.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down' : self.get_image(0,96),
            'left' : self.get_image(0, 96),
            'right': self.get_image(0, 32),
            'up' : self.get_image(0,64)
        }

    def change_anim(self, name): 
        self.image = self.images[name]
        self.image.set_colorkey([255, 255, 255])

    def move_right(self):
        self.position[0] += 3* 0.8
    
    def move_left(self):
        self.position[0] -= 3* 0.8
    
    def move_up(self):
        self.position[1] -= 3* 0.8
    
    def move_down(self):
        self.position[1] += 3* 0.8
    
    def move_upAndright(self):
        self.position[0] += 2.115* 0.8
        self.position[1] -= 2.115* 0.8
    
    def move_upAndleft(self):
        self.position[0] -=2.115 * 0.8
        self.position[1] -= 2.115* 0.8
    
    def move_downAndleft(self):
        self.position[0] -= 2.115* 0.8
        self.position[1] += 2.115* 0.8
    
    def move_downAndright(self):
        self.position[0] += 2.115* 0.8
        self.position[1] += 2.115* 0.8

    def bougepas(self):
        self.position[0] -= 0
        self.position[1] -= 0

        
    def update(self):
        self.rect.topleft = self.position
        

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image
    
   