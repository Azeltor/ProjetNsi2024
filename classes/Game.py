import pygame
import pytmx
import pyscroll
from Fonctions.jeu import *
from Constantes import constante_partie as cp
from classes.Joueur import Player
from classes.Joueur import NPC


class Game:
    def __init__(self, nom):
        cp.NomEcranJeu = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE)
        self.map = nom
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.npc = [NPC("robin", 2)]
        self.player = Player()  #50 * 32, 80* 32
        self.teleport_npcs(self.map)
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        for pnj in npc:
            self.group.add(pnj)
        enter_grotte = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'))
        self.enter_grotte_rect = (pygame.Rect(enter_grotte[0].x, enter_grotte[0].y, enter_grotte[0].width, enter_grotte[0].height),pygame.Rect(enter_grotte[1].x, enter_grotte[1].y, enter_grotte[1].width, enter_grotte[1].height))

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

    def teleport_npcs(self, map):
        for pnj in self.npc:
            NPC.load_points(npc, map)
            NPC.teleport_spawn()

    def switch_grotte(self, indice):
        tmx_data = pytmx.util_pygame.load_pygame('maps/grotte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.map = "grotte"
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  3)
        self.group.add(self.player)

        enter_grotte = (tmx_data.get_object_by_name('dedans1'), tmx_data.get_object_by_name('dedans2'))
        self.enter_grotte_rect = (pygame.Rect(enter_grotte[0].x, enter_grotte[0].y, enter_grotte[0].width, enter_grotte[0].height),pygame.Rect(enter_grotte[1].x, enter_grotte[1].y, enter_grotte[1].width, enter_grotte[1].height))

        dedans_spawn_point = (tmx_data.get_object_by_name('dedans1'), tmx_data.get_object_by_name('dedans2'))
        self.player.position[0] = dedans_spawn_point[indice].x
        self.player.position[1] = dedans_spawn_point[indice].y - 40

    def switch_world(self, indice):
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.map = "world"

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  3)
        self.group.add(self.player)

        enter_grotte = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'))
        self.enter_grotte_rect = (pygame.Rect(enter_grotte[0].x, enter_grotte[0].y, enter_grotte[0].width, enter_grotte[0].height),pygame.Rect(enter_grotte[1].x, enter_grotte[1].y, enter_grotte[1].width, enter_grotte[1].height))

        dehors_spawn_point = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'))
        self.player.position[0] = dehors_spawn_point[indice].x
        self.player.position[1] = dehors_spawn_point[indice].y+20

    def update(self):
        self.group.update()
        a = 0
        if self.map == "world" and self.player.feet.colliderect(self.enter_grotte_rect[0]):
                self.switch_grotte(0)
        if self.map == "grotte" and self.player.feet.colliderect(self.enter_grotte_rect[0]):
                self.switch_world(0)
        if self.map == "world" and self.player.feet.colliderect(self.enter_grotte_rect[1]):
                self.switch_grotte(1)
        if self.map == "grotte" and self.player.feet.colliderect(self.enter_grotte_rect[1]):
                self.switch_world(1)
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
