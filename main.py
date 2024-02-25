'''Fichier Pour La Conception Du Menu'''
import pygame, os
SonMenu = 'Son\somambiant.mp3'
from classes.Bouton import Button
from Constantes import constante_partie as cp
from Fonctions import jeu
from classes.Game import Game





pygame.init()
jeu.fenetre('Menu', 'TitreMenu')
jeu.musiquemenu()
jeu.menu()













