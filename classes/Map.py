from dataclasses import dataclass
import pygame as pg
import pytmx, pyscroll
from Constantes import constante_partie as cp


@dataclass
class Map:
    name: str
    walls: list[pg.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap

class MapManager: #Initialisation de la carte
    def __init__(self, player):
        self.maps = dict()
        self.current_map = "world"
        self.player = player
        self.register_map("world")
        self.register_map("grotte")
        self.teleport_player()
    
    def check_collisions(self):
        self.get_group().update()
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self): #Téléporte le joueur
        self.player.position[0] = 50 * 32
        self.player.position[1] =  80* 32
        self.player.save_location()


    def register_map(self, name):
        tmx_data = pytmx.util_pygame.load_pygame(f"maps/{name}.tmx") #Charge la map dans le dossier maps grâce àson nom
        map_data = pyscroll.data.TiledMapData(tmx_data) #Récupère les datas de la map
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, (cp.screen_width, cp.screen_height)) #Récupère les différentes couches de la carte
        map_layer.zoom = 2 #Zoom sur la carte
        group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer =  10)
        group.add(self.player)
        walls = [] #Initialise une liste vide pour les collisions
        for obj in tmx_data.objects:
            if obj.type == "collision": #Si le type de l'objet sur la carte est "collision"
                walls.append(pg.Rect(obj.x, obj.y, obj.width, obj.height)) #Ajoute à la liste le rectangle de l'objet dans la liste
        self.maps[name] = Map(name, walls, group, tmx_data) #Donne des attributs à la carte
    
    def get_map(self): 
        return self.maps[self.current_map]

    def get_group(self): 
        return self.get_map().group

    def get_walls(self): 
        return self.get_map().walls

    def get_object(self, name): 
        return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self): #Méthode qui dessine la carte
        self.get_group().draw(cp.NomEcranJeu)
        self.get_group().center(self.player.rect.center)

    def update(self): #Permet d'update pour checker les collisions
        self.get_group().update()
        self.check_collisions()
