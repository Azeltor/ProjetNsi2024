import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y): #Définit les coordonnées d'apparition du joueur 
        super().__init__()
        self.sprite_sheet = pygame.image.load('Graphisme\Character\Prototype_Worksheet.png') #Charge la spritesheet avec les personnages
        self.image = self.get_image(0, 0) #Personnage en Idle
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y] #Position du joueur
        self.images = {
            'down' : self.get_image(0,96),
            'left' : self.get_image(0, 96),
            'right': self.get_image(0, 32),
            'up' : self.get_image(0,64)
        } #Différentes images pour les actions différentes du joueur
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8) #Créer un rectangle aux pieds du joueur
        self.old_position = self.position.copy() #Copie la position actuelle du joueur pour la stocker (Initialisation)

    def save_location(self): 
        self.old_position = self.position.copy() #Copie la position actuelle du joueur pour la stocker

    def change_anim(self, name): #Méthode qui s'occupe des animations du personnage
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
        self.feet.midbottom = self.rect.midbottom

    def move_back(self): #Peermet de revenir à la position d'avant (utile pour les collisions)
        self.position = self.old_position
        self.rect.topleft =self.position
        self.feet.midbottom = self.rect.midbottom

        

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image
    
   
