import pygame
from classes.quete import *
pygame.init()



class boite_dialogue:
  X_POSITION = 60
  Y_POSITION = 470


  def __init__(self):
    pygame.init()
    self.box = pygame.image.load('Graphisme\Objet\dialog_box.png')
    self.box = pygame.transform.scale(self.box, (700, 100))
    self.texts = []
    self.text_index = 0
    self.font = pygame.font.Font("Graphisme\Objet\dialog_font.ttf", 18)
    self.etat = False

  def execute(self, dialog = [f"{NPC.name} Je vous ai deja donner la quete '{self.titre}', tete de neuille.")] ) 
    if self.etat:
      self.prochain_text()
    else:
      self.etat = True
      self.text_index = 0
      self.texts = dialog

  def render(self, screen):
    if self.etat:
      screen.blit(self.box,(self.X_POSITION,self.Y_POSITION))
      text = self.font.render(self.texts[self.text_index],False,(0, 0, 0))
      screen.blit(text,(self.X_POSITION + 60,self.Y_POSITION + 30))


  def prochain_text(self):
    self.text_index += 1
    if self.text_index >= len(self.texts) :
      self.etat = False
      
    
  
  
