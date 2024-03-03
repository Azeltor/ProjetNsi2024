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
        if pressed[pygame.K_z] and pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.move_up()
            #self.player.change_anim('up')
        elif pressed[pygame.K_d] and pressed[pygame.K_q] and pressed[pygame.K_s]:
            self.player.move_down()
            #self.player.change_anim('down')
        elif pressed[pygame.K_z] and pressed[pygame.K_d]:
            self.player.move_upAndright()
            #self.player.change_anim('right')
        elif pressed[pygame.K_z] and pressed[pygame.K_q]:
            self.player.move_upAndleft()
            #self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            self.player.move_downAndright()
            #self.player.change_anim('right')
        elif pressed[pygame.K_s] and pressed[pygame.K_q]:
            self.player.move_downAndleft()
            #self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_z]:
            self.player.bougepas()
        elif pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.bougepas()
        
        elif pressed[pygame.K_z]:
            self.player.move_up()
            #self.player.change_anim('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            #self.player.change_anim('down')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            #self.player.change_anim('right')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            #self.player.change_anim('left')
        
 
    def update(self):
        self.map_manager.update()
        


    def run(self):
        while True:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            cp.timer.tick(cp.fps)
    pygame.quit()
