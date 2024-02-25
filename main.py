'''Fichier Pour La Conception Du Menu'''
import pygame, os
from classes.Bouton import Button
from Constantes import constante_partie as cp
from Fonctions import jeu



'''Création Fenêtre Pour menu'''
pygame.init()
jeu.fenetre('Menu', 'menu')
jeu.menu()



