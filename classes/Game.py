import pygame
import pytmx
import pyscroll
from Fonctions.jeu import *
from Constantes import constante_partie as cp
from classes.Joueur import Player



class Game:
    def __init__(self):
        cp.NomEcranJeu = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE)
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.player = Player(50 * 32, 80* 32)
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        enter_grotte = tmx_data.get_object_by_name('dehors1')
        self.enter_grotte_rect = pygame.Rect(enter_grotte.x, enter_grotte.y, enter_grotte.width, enter_grotte.height)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z] and pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.move_up() #Lorsque le joueur appuie sur "Z","D" et "Q" en même temps, le personnage avance vers le haut
            self.player.change_anim('up')
        elif pressed[pygame.K_d] and pressed[pygame.K_q] and pressed[pygame.K_s]:
            self.player.move_down() #Lorsque le joueur appuie sur "D","Q"  et "S" en même temps, le personnage avance vers le bas
            self.player.change_anim('down')
        elif pressed[pygame.K_s] and pressed[pygame.K_z]:
            self.player.bougepas() #Lorsque le joueur appuie sur "S" et "Z", le personnage reste immobile
        elif pressed[pygame.K_d] and pressed[pygame.K_q]:
            self.player.bougepas() #Lorsque le joueur appuie sur "D" et "Q", le personnage reste immobile

        elif pressed[pygame.K_s] and pressed[pygame.K_q]:
            self.player.move_downAndleft() #Lorsque le joueur appuie sur "S" et "Q", le personnage avance vers la gauche
            self.player.change_anim('left')
        elif pressed[pygame.K_z] and pressed[pygame.K_d]:
            self.player.move_upAndright() #Lorsque le joueur appuie sur "Z" et "D", le personnage avance vers la droite
            self.player.change_anim('right')
        elif pressed[pygame.K_z] and pressed[pygame.K_q]:
            self.player.move_upAndleft() #Lorsque le joueur appuie sur "Z" et "Q", le personnage avance vers la gauche
            self.player.change_anim('left')
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            self.player.move_downAndright() #Lorsque le joueur appuie sur "S" et "D", le personnage avance vers la droite
            self.player.change_anim('right')

        elif pressed[pygame.K_z]:
            self.player.move_up() #Lorsque le joueur appuie sur "Z", le personnage avance vers le haut
            self.player.change_anim('up')
        elif pressed[pygame.K_s]:
            self.player.move_down() #Lorsque le joueur appuis sur "S", le personnage avance vers le bas
            self.player.change_anim('down')
        elif pressed[pygame.K_d]:
            self.player.move_right() #Lorsque le joueur appuie sur "D", le personnage avance vers la droite
            self.player.change_anim('right')
        elif pressed[pygame.K_q]:
            self.player.move_left() #Lorsque le joueur appuie sur "Q", le personnage avabce vers la gauche
            self.player.change_anim('left')

    def switch_grotte(self):
        tmx_data = pytmx.util_pygame.load_pygame('maps/grotte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        enter_grotte = tmx_data.get_object_by_name('dedans1')
        self.enter_grotte_rect = pygame.Rect(enter_grotte.x, enter_grotte.y, enter_grotte.width, enter_grotte.height)
        dedans1_spawn_point = tmx_data.get_object_by_name('dedans1')
        self.player.position[0] = dedans1_spawn_point.x
        self.player.position[1] = dedans1_spawn_point.y


    def switch_world(self):
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        enter_grotte = tmx_data.get_object_by_name('dehors1')
        self.enter_grotte_rect= pygame.Rect(warp_grotte1.x, warp_grotte1.y, warp_grotte1.width, warp_grotte1.height)
        dedans1_spawn_point = tmx_data.get_object_by_name('dehors1')
        self.player.position[0] = dehors1.x
        self.player.position[1] = dehors1.y +20


    def update(self):
        self.group.update()
        if self.player.feet.colliderect(self.enter_grotte_rect):
            self.switch_grotte()
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) >  -1:
                sprite.move_back()





    def run(self):
        while True:

            self.player.save_location() #Permet d'obtenir les coordonnées du joueur
            self.handle_input() #Détecte les mouvements du joueur
            self.update() #Appel Update
            self.group.center(self.player.rect.center)
            self.group.draw(cp.NomEcranJeu)
            pygame.display.flip() #Actualiser l'affichage de la map


            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Si le bouton "Quitter" a été cliqué, le jeu se ferme
                    pygame.quit()
            cp.timer.tick(cp.fps)
    pygame.quit() #Permet de quitter le jeu
