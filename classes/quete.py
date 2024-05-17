class Quete:
    def __init__(self, titre, description, objets_requis):
        self.titre = titre
        self.description = description
        self.objets_requis = objets_requis
        self.completee = False



    def proposer_quete(self,joueur):
      si il a pas de quete alors , proposer la quete qui sera stocker dans un dico 
      ex : quete1, quete2 , quete3 , quete4 ---> vont être créer a la main
      

    def verifier_completion(self, joueur):
        for objet in self.objets_requis:
            if not joueur.possede_objet(objet):
                print(f"{joueur.nom} n'a pas encore tous les objets nécessaires pour compléter la quête '{self.titre}'.")
                return False
        self.completee = True
        print(f"{joueur.nom} a complété la quête '{self.titre}'!")
        return True

    def __str__(self):
        return f"Quête: {self.titre}\nDescription: {self.description}\nObjets requis: {', '.join(self.objets_requis)}"

# A ajouter dans la classe joueur : self.
