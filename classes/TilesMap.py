import pygame, sys
from pytmx.util_pygame import load_pygame
pygame.init()

class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos) 