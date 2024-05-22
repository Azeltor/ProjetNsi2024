import pygame
import pytmx
import pyscroll
from Fonctions.jeu import *
from Constantes import constante_partie as cp
from classes.Dialogue import *
from classes.Joueur import Player
from classes.Joueur import NPC


class Game:
    def __init__(self, nom, nomfenetre):
        self.screen = pygame.display.set_mode((cp.screen_width - 10, cp.screen_height - 50),pygame.RESIZABLE)
        self.map = nom
        pygame.display.set_caption(nomfenetre)
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        map_layer.zoom = 2
        self.npc = [NPC("robin_rouge", 2, []), NPC("personnage_00", 2, [])]
        self.player = Player()  #50 * 32, 80* 32
        self.teleport_npcs(self.map)
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        for pnj in self.npc:
            self.group.add(pnj)
        
        enter_grotte = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'))
        self.enter_grotte_rect = (pygame.Rect(enter_grotte[0].x, enter_grotte[0].y, enter_grotte[0].width, enter_grotte[0].height),pygame.Rect(enter_grotte[1].x, enter_grotte[1].y, enter_grotte[1].width, enter_grotte[1].height))


        enter_foret = tmx_data.get_object_by_name('Foret1')
        self.enter_foret_rect = pygame.Rect(enter_foret.x, enter_foret.y, enter_foret.width, enter_foret.height)

        enter_cimetierre = tmx_data.get_object_by_name('Cimetierre1')
        self.enter_cimetierre_rect = pygame.Rect(enter_cimetierre.x, enter_cimetierre.y, enter_cimetierre.width, enter_cimetierre.height)
        self.boite_dialogue = boite_dialogue()
        
        
                        
                    

                    

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
            
        elif pressed[pygame.K_s]:
            self.player.move_down() #Lorsque le joueur appuis sur "S", le personnage avance vers le bas
            
        elif pressed[pygame.K_d]:
            self.player.move_right() #Lorsque le joueur appuie sur "D", le personnage avance vers la droite
            
        elif pressed[pygame.K_q]:
            self.player.move_left() #Lorsque le joueur appuie sur "Q", le personnage avabce vers la gauche
            

    def teleport_npcs(self, map):
        for pnj in range(len(self.npc)):
            self.npc[pnj].load_points(self.map)
            self.npc[pnj].teleport_spawn()

    def switch_grotte(self, indice):
        tmx_data = pytmx.util_pygame.load_pygame('maps/grotte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
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
        self.npc = []
        self.teleport_npcs(self.map)

    def switch_world(self, indice):
        tmx_data = pytmx.util_pygame.load_pygame('maps/world.tmx')
        pygame.display.set_caption('Numeric Project v1.0')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
        map_layer.zoom = 2
        self.map = "world"

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        self.group.add(self.player)
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        
        dehors_spawn_point = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'), tmx_data.get_object_by_name('Foret1'), tmx_data.get_object_by_name('Cimetierre1'))
        self.player.position[0] = dehors_spawn_point[indice].x 
        self.player.position[1] = dehors_spawn_point[indice].y + 30

        enter_grotte = (tmx_data.get_object_by_name('dehors1'), tmx_data.get_object_by_name('dehors2'))
        self.enter_grotte_rect = (pygame.Rect(enter_grotte[0].x, enter_grotte[0].y, enter_grotte[0].width, enter_grotte[0].height),pygame.Rect(enter_grotte[1].x, enter_grotte[1].y, enter_grotte[1].width, enter_grotte[1].height))

        enter_foret = tmx_data.get_object_by_name('Foret1')
        self.enter_foret_rect = pygame.Rect(enter_foret.x, enter_foret.y, enter_foret.width, enter_foret.height)

        enter_cimetierre = tmx_data.get_object_by_name('Cimetierre1')
        self.enter_cimetierre_rect = pygame.Rect(enter_cimetierre.x, enter_cimetierre.y, enter_cimetierre.width, enter_cimetierre.height)

       
        
        
        


        self.npc = [NPC("robin", 2), NPC("personnage_00", 2)]
        self.teleport_npcs(self.map)
        for pnj in self.npc:
            self.group.add(pnj)

    def switch_foret(self, indice):
        tmx_data = pytmx.util_pygame.load_pygame('maps/foret.tmx')
        pygame.display.set_caption('Numeric Project v1.0')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
        map_layer.zoom = 2
        self.map = "foret"

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  1)
        self.group.add(self.player)

        enter_foret = (tmx_data.get_object_by_name('Foret2'), tmx_data.get_object_by_name('Cache1'), tmx_data.get_object_by_name('Cache2') )
        self.enter_foret_rect = (pygame.Rect(enter_foret[0].x, enter_foret[0].y, enter_foret[0].width, enter_foret[0].height), pygame.Rect(enter_foret[1].x, enter_foret[1].y, enter_foret[1].width, enter_foret[1].height), pygame.Rect(enter_foret[2].x, enter_foret[2].y, enter_foret[2].width, enter_foret[2].height))

        dehors_spawn_point = (tmx_data.get_object_by_name('Foret2'), tmx_data.get_object_by_name('Cache2'), tmx_data.get_object_by_name('Cache1'))
        self.player.position[0] = dehors_spawn_point[indice].x
        self.player.position[1] = dehors_spawn_point[indice].y
    
    def switch_cimetierre(self):
        tmx_data = pytmx.util_pygame.load_pygame('maps/Cimetierre.tmx')
        pygame.display.set_caption('Numeric Project v1.0')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height))
        pygame.display.set_icon(pygame.image.load('Graphisme\Logo Menu\LogoMieux.png')) #Chargement du logo
        map_layer.zoom = 2
        self.map = "cimetierre"

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  1)
        self.group.add(self.player)

        enter_cimetierre = tmx_data.get_object_by_name('Cimetierre2')
        self.enter_cimetierre_rect = pygame.Rect(enter_cimetierre.x, enter_cimetierre.y, enter_cimetierre.width, enter_cimetierre.height)

        dehors_spawn_point = tmx_data.get_object_by_name('Cimetierre2')
        self.player.position[0] = dehors_spawn_point.x  + 30
        self.player.position[1] = dehors_spawn_point.y 
        
        
    def update(self):
        self.group.update()

        if self.map == 'world' and self.player.feet.colliderect(self.enter_cimetierre_rect):
            self.switch_cimetierre()
            self.player.position[0] += 40
        if self.map == 'cimetierre' and self.player.feet.colliderect(self.enter_cimetierre_rect):
            self.switch_world(3)
            self.player.position[0] = 87* 32
            self.player.position[1] = 29* 32
        if self.map == 'foret' and self.player.feet.colliderect(self.enter_foret_rect[0]):
            self.switch_world(2)
        if self.map == 'world' and self.player.feet.colliderect(self.enter_foret_rect):
            self.switch_foret(0)
            self.player.position[1] -= 40
        if self.map == 'foret' and self.player.feet.colliderect(self.enter_foret_rect[1]):
            self.switch_foret(1) 
            self.player.position[0] -= 40
            self.player.position[1] += 40
        if self.map == 'foret' and self.player.feet.colliderect(self.enter_foret_rect[2]):
            self.switch_foret(2)
            self.player.position[1] += 40
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
        for pnj in range(len(self.npc)):
            if self.player.feet.colliderect(self.enter_grotte_rect[1]):
                self.npc[pnj].bougepas()
            else:
                self.npc[pnj].move()

    def collisionnpc(self, boite_dialogue):
        for sprite in self.group.sprites():
            if type(sprite) is NPC:
                    if sprite.feet.colliderect(self.player.rect):
                        sprite.speed = 0
                        if Entity.quete_actuelle == None:
                            for i in range(len(self.npc)):
                                if self.npc[i].name == sprite: ## Attention pas sûr que ça soit sprite.name
                                    proposer_quete(self.player,self.npc[i])
                        if Entity.verifier_completion(self.player):
                           dialogue.boite_dialogue.texts = "la quête est accomplit Neuille ! "
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    boite_dialogue.execute(sprite.dialogue)
                    else:
                        sprite.speed = 0.3
            




    def run(self):
        while True:

            self.player.save_location() #Permet d'obtenir les coordonnées du joueur
            self.handle_input() #Détecte les mouvements du joueur
            self.update() #Appel Update
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            self.boite_dialogue.render(self.screen)
            self.collisionnpc(self.boite_dialogue)
            pygame.display.flip() #Actualiser l'affichage de la map
             


            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Si le bouton "Quitter" a été cliqué, le jeu se ferme
                    pygame.quit()
                

            
            cp.timer.tick(cp.fps)
    pygame.quit() #Permet de quitter le jeu
