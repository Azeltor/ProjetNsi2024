import pygame, sys
from classes.Game import Game

class Entity(pygame.sprite.Sprite):
    def __init__(self, name, x, y): #Définit les coordonnées d'apparition du joueur 
        super().__init__()
        self.sprite_sheet = pygame.image.load(f"Graphisme\Character\{name}.png") #Charge la spritesheet avec les personnages
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
        self.inventaire = []
        self.quete_actuelle = None
        
    def save_location(self):
        self.old_position = self.position.copy() #Copie la position actuelle du joueur pour la stocker

    def change_anim(self, name): #Méthode qui s'occupe des animations du personnage
        self.image = self.images[name] 
        self.image.set_colorkey([255, 255, 255])

    def move_right(self): #Fonction pour avancer à droite
        self.position[0] += 3* 0.8 #Valeur de déplacement vers la droite
    
    def move_left(self): #Fonction pour avancer à gauche
        self.position[0] -= 3* 0.8 #Valeur de déplacement vers la gauche
    
    def move_up(self): #Fonction pour avancer en haut
        self.position[1] -= 3* 0.8 #Valeur de déplacement vers le haut
    
    def move_down(self): #Fonction pour avancer en bas
        self.position[1] += 3* 0.8 #Valeur de déplacement vers le bas
    
    def move_upAndright(self): #Fonction pour avancer en haut à droite
        self.position[0] += 2.115* 0.8 #Valeur de déplacement vers la droite
        self.position[1] -= 2.115* 0.8 #Valeur de déplacement vers le haut
    
    def move_upAndleft(self): #Fonction pour avancer en haut à gauche
        self.position[0] -=2.115 * 0.8 #Valeur de déplacement vers la gauche
        self.position[1] -= 2.115* 0.8 #Valeur de déplacement vers le haut
    
    def move_downAndleft(self): #Fonction pour avancer en bas à gauche
        self.position[0] -= 2.115* 0.8 #Valeur de déplacement vers la droite
        self.position[1] += 2.115* 0.8 #Valeur de déplacement vers le bas
    
    def move_downAndright(self): #Fonction pour avancer en haut à droite
        self.position[0] += 2.115* 0.8 #Valeur de déplacement vers le bas
        self.position[1] += 2.115* 0.8 #Valeur de déplacement vers la droite

    def bougepas(self): #Fonction permettant d'immobiliser le personnage
        self.position[0] -= 0
        self.position[1] -= 0

        
    def update(self): #Permet d'actualiser la position du joueur
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self): #Permet de revenir à la position d'avant (utile pour les collisions)
        self.position = self.old_position
        self.rect.topleft =self.position
        self.feet.midbottom = self.rect.midbottom

        

    def get_image(self, x, y): #Permet d'actualiser la map lorsque le joueur avance
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image
    
   
class Player(Entity):
    def __init__(self):
        super().__init__("test", 50*32, 80*32)
        
class NPC(Entity):
    def __init__(self, name, nb_points):
        super().__init__(name, 50*32, 80*32)
        self.nb_points = nb_points
        self.name = name
        self.points = []
        self.current_point = 0
        
    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
        
    def load_points(self, map):
        for k in range(1, self.nb_points + 1):
            point = (Game.tmx_data.get_object_by_name(str(self.name)+'_path'+str(k)))
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)