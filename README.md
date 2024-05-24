Projet NSI  Tom/Evan/Gabriel/Baptiste

1.Présentation du projet.
Vous décrivez votre projet, explications des règles du jeu éventuelles, captures d’écran …


C’est un RPG où on doit remplir des quêtes en trouvant des objets à travers les cartes. Il y a 4 zones différentes à explorer pour l’instant.
Touches pour jouer :
-Z : aller vers le haut
-Q : aller vers la gauche
-S : aller vers le bas
-D : aller vers la droite
-Espace : interagir avec les PNJ (il faut se coller à eux)
-E : Accepter les quêtes (une fois dans les dialogues) ou ouvrir les coffres


-Capture d'écran : 
![image](https://github.com/EvanMyDu/ProjetNsi2024/assets/160437266/7cd610c0-502c-4397-812f-294b6b032483)
![image](https://github.com/EvanMyDu/ProjetNsi2024/assets/160437266/d76214d2-0042-484c-aac6-cac20a81659c)
![image](https://github.com/EvanMyDu/ProjetNsi2024/assets/160437266/395656ca-36e8-4842-a791-47b4cb5b59e7)


2.Description du code
Vous décrivez la doc de vos classes/fonctions/méthodes. Vous ferez le lien avec la description faite dans le point précédent.

I : Classe 
		Dialogue : Fait
Cette classe sert principalement à faire apparaître les dialogues , c'est-à-dire qu’une bulle de texte va apparaître à certaines coordonnées si la touche espace est appuyer. Cette classe va être utilisée avec la fonction de collision npc dans la classe game , et on va vérifier 3 conditions grâce notamment à la fonction de la classe Quête,  vérifier completion. On va alors regarder: 
-Si le joueur n’a pas de quête 
-Si le joueur n’a pas les objets requis pour compléter la quête 
-Si le joueur à déjà fini la quête 
	On va pouvoir permettre de créer et d’adapter les dialogues en fonction des
	conditions. 

	Quête: En cours, 
		Cette classe permet de créer différente quête qui seront attribués
	au différents pnj dans la classe game avec self.npc 
	Objet : En cours,
		Cette classe créer les différents objet présent sur la map qui sont
nécessaire pour rendre une quête, elle  permet de ramasser un objet , de le placer dans self.inventaire du joueur pour pouvoir vérifier la présence des objets pour valider les quêtes.
	
Vie : En cours,
		Cette classe permet de créer une barre de vie au joueur , dans
l’optique de créer des combats tour par tour. 
			
	Map :  Fait
Cette classe permet d’initialiser la map du jeu, permet de savoir si le joueur rentre en collision avec un objet, téléporte le joueur lorsque le joueur passe de la grotte a dehors 

Animation : En cours
			Cette classe permet d’animer le personnage lorsqu’il marche par
                                     exemple à droite, le spritesheet va s’update pour prendre l’animation
			du personnage qui marche à droite

	Joueur: Fait
Cette classe permet de définir les coordonnées  du joueur afin
de savoir où il se trouve sur la map pour pouvoir savoir si le joueur est en collision avec un mur. Si c’est le cas, le joueur sera reculer avec la fonction “move back” et immobilisé avec la fonction “bouge pas” permettant  de le faire revenir à la position d'avant. Elle permet également de stocker la position du joueur à chaque fois que le personnage bouge mais aussi les fonctions permettant de se déplacer vers la droite, gauche, bas,haut, haut droite, haut gauche, bas gauche, bas droite. C’est aussi avec l’héritage de cette classe qu’on a fait les pnjs


Game : Fait
Cette classe gère le fonctionnement global et le processus du jeu. Elle est responsable de l'initialisation de la fenêtre de jeu, du chargement des cartes et des ressources du jeu, de la gestion des entrées et sorties des joueurs entre les maps, de la gestion des PNJ (personnages non-joueurs) et de la commutation entre les différentes cartes du jeu. 



Bouton: Fait
Cette classe Bouton est conçue pour créer des boutons interactifs. Elle permet de définir la position et l'apparence d'un bouton en important l’image qu’elle va mettre à la bonne échelle, puis elle va l’afficher sur l'écran. Ensuite elle va détecter si le curseur de la souris est sur le bouton et permet d’effectuer des actions avec des clics.


3.Attribution des rôles
Vous associez à chaque partenaire de votre équipe le ou les rôles joués dans l’écriture et la réalisation du projet.
Ecriture du code, graphismes, idées …

Lire le readme dans le fichier script pour plus de détail

Ecriture des Fonctions : 
Menu : Evan, Gabriel, Baptiste
Animation : Evan , Gabriel
Vie : Tom
Bouton : Evan, Gabriel , Baptiste
Dialogue :Tom, Evan
Game : Gabriel , Evan , Tom, Baptiste
Joueur : Gabriel , Evan
Map : Evan, Gabriel 
Objet : Tom 
Quête : Tom, Evan
Correction des bugs : Tous
Jeu : Gabriel, Evan, Baptiste


Graphismes
Logo : Baptiste
Map principale : Gabriel
Menu : Baptiste
Cimetière : Evan
Forêt : Baptiste, Evan
Grotte : Gabriel
PNJ : Baptiste






    

-Le projet n'est pas libre de droit et est réalisé pour un projet en NSI




