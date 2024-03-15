import pygame
import pytmx
import pyscroll
from Fonctions.jeu import *
from Constantes import constante_partie as cp
from classes.Joueur import Player
from classes.Map import *


class Game:
    def __init__(self):
        cp.NomEcranJeu = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE)
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.player)



    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            self.player.move_up() #Lorsque le joueur appuie sur "Z", le personnage avance vers le haut
            #self.player.change_anim('up')
        elif pressed[pygame.K_s]:
            self.player.move_down() #Lorsque le joueur appuis sur "S", le personnage avance vers le bas
            #self.player.change_anim('down')
        elif pressed[pygame.K_d]:
            self.player.move_right() #Lorsque le joueur appuie sur "D", le personnage avance vers la droite
            #self.player.change_anim('right')
        elif pressed[pygame.K_q]:
            self.player.move_left() #Lorsque le joueur appuie sur "Q", le personnage avabce vers la gauche
            #self.player.change_anim('left')
        elif pressed[pygame.K_z] and pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.move_up() #Lorsque le joueur appuie sur "Z","D" et "Q" en même temps, le personnage avance vers le haut
            #self.player.change_anim('up') 
        elif pressed[pygame.K_d] and pressed[pygame.K_q] and pressed[pygame.K_s]:
            self.player.move_down() #Lorsque le joueur appuie sur "D","Q"  et "S" en même temps, le personnage avance vers le bas
            #self.player.change_anim('down')
        elif pressed[pygame.K_z] and pressed[pygame.K_d]:
            self.player.move_upAndright() #Lorsque le joueur appuie sur "Z" et "D", le personnage avance vers la droite
            #self.player.change_anim('right')
        elif pressed[pygame.K_z] and pressed[pygame.K_q]:
            self.player.move_upAndleft() #Lorsque le joueur appuie sur "Z" et "Q", le personnage avance vers la gauche
            #self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            self.player.move_downAndright() #Lorsque le joueur appuie sur "S" et "D", le personnage avance vers la droite
            #self.player.change_anim('right')
        elif pressed[pygame.K_s] and pressed[pygame.K_q]:
            self.player.move_downAndleft() #Lorsque le joueur appuie sur "S" et "Q", le personnage avance vers la gauche
            #self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_z]:
            self.player.bougepas() #Lorsque le joueur appuie sur "S" et "Z", le personnage reste immobile
        elif pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.bougepas() #Lorsque le joueur appuie sur "D" et "Q", le personnage reste immobile
        
 
    def update(self):
        self.map_manager.update() #Update (demander à Evan)
        


    def run(self):
        while True:

            self.player.save_location() #Permet d'obtenir les coordonnées du joueur
            self.handle_input() #Détecte les mouvements du joueur
            self.update() #Appel Update
            self.map_manager.draw() #Permet de dessiner la map
            pygame.display.flip() #Actualiser l'affichage de la map
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Si le bouton "Quitter" a été cliqué, le jeu se ferme
                    pygame.quit()
            cp.timer.tick(cp.fps)
    pygame.quit() #Permet de quitter le jeu
