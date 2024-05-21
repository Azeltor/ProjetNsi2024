import pytmx, pygame, sys

class boite_dialogue:
X_POSITION = 60
Y_POSITION = 470
  
def __init__(self):
  self.box = pygame. image.Load('/dialogs/dialog_box.png')
  self.ecran = pygame. transform.scale(self.dialogue, (700, 100))
  self.texts = ["Salut ça va ?", "moi super bien", "bonne aventure"]
  self.text_index = 0
  self.font = pygame.font.Font("../dialogs/dialog_font.ttf", 18)
  self.etat = True
  
def render(self, screen):
  if self.etat:
    screen.blit(self.boite_dialogue,(self.X_POSITION,self.Y_POSITION))
    text = self.font.render(self.texts[self.text_index],False,(0, 0, 0))
    screen.blit(text,(self.X_POSITION + 60,self.Y_POSITION + 30))


def prochain_text(self):
  self.text_index = 1
  if self.text_index >= len(self.text):
    self.etat = False 
    
    


  
  
