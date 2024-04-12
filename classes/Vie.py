import pygame
class bar_de_vie():
  def __init__(self, x, y, w, h, max_hp):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    #calcule le ratio de vie
    ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
    pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


vie_joueur = bar_de_vie(250, 200, 300, 40, 100)

