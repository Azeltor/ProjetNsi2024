import pygame
pygame.init()


class Button:

   def __init__(self, x, y, image, scale):
      self.coordonnee = (x, y) #coordonnées d'origine l'image
      self.width = image.get_width() #Longeur de l'image
      self.height = image.get_height() #Largeur de l'image
      self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale))) #Taille de l'image
      self.rect = self.image.get_rect()  # Rectangle autour de l'image
      self.rect.topleft = (x - self.width / 2, y) #Zone de clique rectangulaire

   def draw(self, surface):
      surface.blit(self.image, (self.rect.x, self.rect.y)) #On dessine le bouton

   def est_dans(self):
      pos = pygame.mouse.get_pos() #Permet d'avoir la position du curseur
      return self.rect.collidepoint(pos) #Renvoie True si le curseur est dans le bouton, False sinon


   def clique(self, surface):
      self.clicked = False
      action = False #Initialise action en False
      if self.est_dans(): #Si le curseur est dans le bouton
         if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #Si le curseur est dans le bouton et on a pas encore clique gauche
            self.clicked = True #On passe self.clicked en True
            action = True #On execute l'action
      if pygame.mouse.get_pressed()[0] == 0: #Si elle est décliqué
         self.clicked = False #Quand la souris à été cliqué le self.clicked passe en false
      return action #Renvoie False ou True


