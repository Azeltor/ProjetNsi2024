import os, pygame
pygame.init()



os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()


screen_width = info.current_w
screen_height = info.current_h

fps = 60
timer = pygame.time.Clock()

NomEcran = None
NomEcranJeu = None
music_enabled = True

SonMenu = 'Son\somambiant.mp3'

map1 = []
map2 = []
map3 = []

x, y = 0, 0