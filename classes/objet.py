class Object:
    def __init__(self, nom):
        self.nom = nom
        
    def ramasser_objet(self, objet):
        if pressed[pygame.K_e]:
            self.inventaire.append(objet)
        
    def possede_objet(self, nom_objet):
        for objet in self.inventaire:
            if objet.nom == nom_objet:
                return True
        return False
    


        
Epee = Object("Epée")
Bouclier = Object("Boucier")
Chaussures = Object("Chaussure")
bague = Object("bague")
stylo = Object("stylo")
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
   


