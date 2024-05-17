class Objet:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def __str__(self):
        return f"{self.nom}: {self.description}"
      



  
  
  
  
  # Ajouter dans la classe joueur:
# self.inventaire = []
 # Méthodes pour gérer l'inventaire et les quêtes
    def ramasser_objet(self, objet):
        self.inventaire.append(objet)
        print(f"{self.nom} a ramassé {objet.nom}.")

    def possede_objet(self, nom_objet):
        for objet in self.inventaire:
            if objet.nom == nom_objet:
                return True
        return False

    def afficher_inventaire(self):
        print(f"Inventaire de {self.nom}:")
        for objet in self.inventaire:
            print(f" - {objet}")
