import pytmx, pygame, sys

class boite_dialogue(self):
  
def __init__(self):
  self.boite = pygame.image.load('ProjetNsi2024/Graphisme/Objet/dialog_box.png')
  self.font = pygame.font.Font('ProjetNsi2024/Graphisme/Objet/dialog_font.ttf')
  self.text = ""
  self.visible = False

def afficher(self, ecran):
  ecran.blit(self.boite,(0,0))
  
  
