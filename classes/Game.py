import pygame
import pytmx
import pyscroll
from Fonctions.jeu import *
from Constantes import constante_partie as cp
from classes.Joueur import Player


class Game:
    def __init__(self):
        cp.NomEcranJeu = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE)
        tmx_data = pytmx.util_pygame.load_pygame('maps/map_test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        map_layer.zoom = 2
        self.player = Player(77 * 32, 87* 32)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()  
        if pressed[pygame.K_z] and pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.bougepas()
        elif pressed[pygame.K_z] and pressed[pygame.K_d]:
            self.player.move_upAndright()
            self.player.change_anim('right')
        elif pressed[pygame.K_z] and pressed[pygame.K_q]:
            self.player.move_upAndleft()
            self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            self.player.move_downAndright()
            self.player.change_anim('right')
        elif pressed[pygame.K_s] and pressed[pygame.K_q]:
            self.player.move_downAndleft()
            self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_z]:
            self.player.bougepas()
        elif pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.bougepas()
        elif pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_anim('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_anim('down')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_anim('right')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_anim('left')
        

        


    def run(self):
        while True:
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(cp.NomEcranJeu)
            pygame.display.flip()
            self.handle_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

