'''Fichier Pour La Conception Du Menu'''
import pygame, os
SonMenu = 'Son\somambiant.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SonMenu)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.04)
from classes.Bouton import Button
from Constantes import constante_partie as cp
from Fonctions import jeu

import time


'''Création Fenêtre Pour menu'''
pygame.init()
jeu.fenetre()
jeu.menu()

# Créer des instances de bouton



#Action en cas de clic
tuiles = {}


'''def charger_tileset():
  """Charger un tileset
  Associe a chaque tuiles d'un tileset un ID, divise un tileset
  en plusieurs lignes
  Permet de bosser avec Tiled
  """
  # Charger l'image du tileset
  img = pygame.image.load("Graphisme/tiles/tileset.png") #.convert_alpha()
  img_largeur, img_hauteur = img.get_size()  # Prendre les dimensions
  id = 0  # J'initialise les IDs
  for y in range(int(img_hauteur/32)):  # Je parcours les lignes
      for x in range(int(img_largeur/32)):  # Je parcours les colonnes
          rectangle = (x*32, y*32, 32, 32)  # Je divise les tuiles de l'image
          tuiles[str(id)] = img.subsurface(rectangle) # J'ajoute au dictionnaire des tuiles
          id += 1  # J'incrémente les IDs

charger_tileset()'''


# Boucle De jeu


