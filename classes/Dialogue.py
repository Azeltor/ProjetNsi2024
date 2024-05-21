import pytmx, pygame, sys

class boite_dialogue(self):
  
def __init__(self):
  self.boite = pygame.image.load('ProjetNsi2024/Graphisme/Objet/dialog_box.png')
  self.font = pygame.font.Font('ProjetNsi2024/Graphisme/Objet/dialog_font.ttf')
  self.text = ""
  self.visible = False

def afficher(self, ecran):
  if self.visible:
    ecran.blit(self.boite, (50, 400))  # Position de la boîte de dialogue
    text_surface = self.font.render(self.text, True, (0, 0, 0))
    ecran.blit(text_surface, (70, 420))  # Position du texte à l'intérieur de la boîte

  
  
