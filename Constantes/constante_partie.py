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
music_enabled = True #La musique sera jouée par défaut lorsque le joueur est dans le menu

SonMenu = 'Son\somambiant.mp3' #Ajout de la musique présente dans le menu du jeu

