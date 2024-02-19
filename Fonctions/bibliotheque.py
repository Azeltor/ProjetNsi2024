import csv
import os
import valeurs
import pygame

pygame.init()

def charger_tileset():
  """Charger un tileset
  Associe a chaque tuiles d'un tileset un ID, divise un tileset
  en plusieurs lignes
  Permets de bosser avec Tiled
  """
  # Charger l'image du tileset
  img = pg.image.load("Graphisme/tiles/tileset.png").convert_alpha()
  img_largeur, img_hauteur = img.get_size()  # Prendre les dimensions
  id = 0  # J'initialise les IDs
  for y in range(int(img_hauteur/32)):  # Je parcours les lignes
      for x in range(int(img_largeur/32)):  # Je parcours les colonnes
          rectangle = (x*32, y*32, 32, 32)  # Je divise les tuiles de l'image
          # J'ajoute au dictionnaire des tuiles
          valeurs.tuiles[str(id)] = img.subsurface(rectangle)
          id += 1  # J'incrémente les IDs



