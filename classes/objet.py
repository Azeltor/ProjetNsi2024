
class Objet(pygame.sprite.Sprite):
    def __init__(self, nom, x, y):
        self.nom = nom
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def ramasser(self):
        if pressed[pygame.K_e]:
            player.inventaire.append(objet)
            self.kill()  




        
Epee = Objet("Epée")
Bouclier = Objet("Boucier")
Chaussures = Objet("Chaussure")
bague = Objet("bague")
stylo = Objet("stylo")
arc = Objet("Arc")
fleches = Objet("Flèches")
amulette = Objet("Amulette")
potionsoins = Objet("Potion de soin")
tunique = Objet("Tunique")
grimoire = Objet("Grimoire")
heaume = Objet("Heaume")
gants = Objet("Gants")
lanterne = Objet("Lanterne")
sacoche = Objet("Sacoche")
parchemin = Objet("Parchemin")
clef = Objet("Clef")
herbes = Objet("Herbes médicinales")
pain = Objet("Pain")
fromage = Objet("Fromage")
trophée = Objet("Trophée")


    

    



  
  
  
  
  # Ajouter dans la classe joueur:
# self.inventaire = []
 # Méthodes pour gérer l'inventaire et les quêtes
   


