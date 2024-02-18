import pygame, sys, os

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h


#Création de la fenêtre puvant être modifiée
pygame.display.set_caption('Test Jeu')
screen = pygame.display.set_mode((screen_width-10, screen_height-50),pygame.RESIZABLE)

#Icone de jeu et Fond du menu
Imagefond = pygame.image.load('asset\Bg.jpg')
Logo = pygame.image.load('asset\icone.png')
PlayButton = pygame.image.load('asset\R (1).png')
Iconeimg = pygame.image.load('asset\icone.png')
#Time fps
fps = 60
timer = pygame.time.Clock()

#Bouton 

class Bouton:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()  # Rectangle autour de l'image
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


def check_play_button(mouse_pos):
    """Vérifie si le bouton  a été cliqué."""
    if Play.rect.collidepoint(mouse_pos):
        # Si le clic est dans la zone du bouton, quitter le jeu
        pygame.quit()
        sys.exit()
    if Icone.rect.collidepoint(mouse_pos):
        pygame.display.toggle_fullscreen()



# Créer des instances de bouton
Play = Bouton(960.0 - 87.5, 440 - 37.5, PlayButton, 0.05)
Icone = Bouton(1825, 15, Iconeimg, 0.75)

# Boucle De jeu
running = True
while running:
    # Arrière Plan
    timer.tick(fps)
    screen.blit(Imagefond, (0, 0))

    for event in pygame.event.get():  # Récupère les actions du joueur
        if event.type == pygame.QUIT:  # Si le joueur veut quitter la fenêtre
            running = False
            print('Le jeu se ferme')
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Si un clic de souris est détecté # Si le clic est le bouton gauche de la souris
            check_play_button(event.pos)  # Vérifie si le bouton a été cliqué

    # Dessiner les boutons
    Play.draw(screen)
    Icone.draw(screen)

    pygame.display.update()

pygame.quit()  # Ferme la fenêtre
