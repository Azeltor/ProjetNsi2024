import pytmx, pygame, sys
from classes.Animation import *

class Entity(AnimateSprite):
    def __init__(self, name, x, y): #Définit les coordonnées d'apparition du joueur 
        super().__init__(name)
        
        self.image = self.get_image(0, 0) #Personnage en Idle
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y] #Position du joueur
        
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8) #Créer un rectangle aux pieds du joueur
        self.old_position = self.position.copy() #Copie la position actuelle du joueur pour la stocker (Initialisation)
        self.inventaire = []
        self.quete_actuelle = None

    
                    

    def save_location(self):
        self.old_position = self.position.copy() #Copie la position actuelle du joueur pour la stocker

    

    def move_right(self): #Fonction pour avancer à droite
        self.change_anim('right')
        self.position[0] += 3* 0.8 #Valeur de déplacement vers la droite
        
    def move_left(self): #Fonction pour avancer à gauche
        self.change_anim('left')
        self.position[0] -= 3* 0.8 #Valeur de déplacement vers la gauche
        
    def move_up(self): #Fonction pour avancer en haut
        self.change_anim('up')
        self.position[1] -= 3* 0.8 #Valeur de déplacement vers le haut
        
    def move_down(self): #Fonction pour avancer en bas
        self.change_anim('down')
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
        super().__init__("robin_rouge", 49*32, 80*32)
        
class NPC(Entity):
    def __init__(self, name, nb_points, dialogue):
        super().__init__(name, 50*32, 80*32)
        self.nb_points = nb_points
        self.name = name
        self.points = []
        self.current_point = 0
        self.speed = 0.3
        self.dialogue = dialogue
        self.direction = 1  # 1 for forward, -1 for backward

    def move(self):
        current_point = self.current_point
        next_point = self.current_point + self.direction
        
        if next_point >= self.nb_points or next_point < 0:
            self.direction *= -1  # Invert direction
            next_point = self.current_point + self.direction

        current_rect = self.points[current_point]
        next_rect = self.points[next_point]

        tolerance = 3  # Tolerance for reaching the point
        if abs(self.position[1] - next_rect.y) <= tolerance and abs(self.position[0] - next_rect.x) <= tolerance:
            self.current_point = next_point
            self.position[0] = next_rect.x
            self.position[1] = next_rect.y

        if self.position[1] < next_rect.y:
            self.change_anim('down')
            self.position[1] += 3 * self.speed
        elif self.position[1] > next_rect.y:
            self.change_anim('up')
            self.position[1] -= 3 * self.speed
        elif self.position[0] < next_rect.x:
            self.change_anim('right')
            self.position[0] += 3 * self.speed
        elif self.position[0] > next_rect.x:
            self.change_anim('left')
            self.position[0] -= 3 * self.speed

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()
        
    def load_points(self, map):
        for k in range(1, self.nb_points + 1):
            point = pytmx.util_pygame.load_pygame('maps/' + str(map) + '.tmx').get_object_by_name(str(self.name) + '_path' + str(k))
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)