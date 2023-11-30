from random import randint
import pyxel

class Mobile:
    def __init__(self):
        """
        Le mobile est représenté par une forme carrée.
        origine des positions : coin haut gauche du carré
        mesure du côté : long_x et long_y
        """
        # attributs pour la position initiale du mobile : x, y
        self.x = 60
        self.y = 60
        
        # attributs pour la taille du mobile : long_x, long_y
        self.long_x = 8
        self.long_y = 8
    
    def grossir(self):
        """Le mobile grossit. Cela se traduit par une augmentation de sa taille, hauteur et largeur, de 1 pixel."""

        self.long_x += 1
        self.long_y += 1

    def maigrir(self):
        """Lorsque le maigrit. Cela se traduit par une diminution de sa taille, hauteur et largeur, de 1 pixel."""

        if self.long_x > 2:
            self.long_x += -1
            self.long_y += -1

    def deplacement_droite(self):
        """A chaque pression sur la touche flèche droite, le mobile se déplace de 1 pixel à droite
        L'abscisse x du mobile est modifiée de la valeur +1."""

        if self.x < 128 - self.long_x:
            self.x += 1
    
    def deplacement_gauche(self):
        """A chaque pression sur la touche flèche gauche, le mobile se déplace de 1 pixel à gauche
        L'abscisse x du mobile est modifiée de la valeur -1."""

        if self.x > 0:
            self.x += -1

    def deplacement_haut(self):
        """A chaque pression sur la touche flèche haut, le mobile se déplace de 1 pixel vers le haut. L'ordonnée y 
        du mobile est modifiée de la valeur -1 (les valeurs positives sont orientées vers le bas de l'écran)."""

        if self.y > 0:
            self.y += -1
    
    def deplacement_bas(self):
        """A chaque pression sur la touche flèche bas, le mobile se déplace de 1 pixel vers le bas
        L'ordonnée du mobile est modifiée de la valeur +1."""

        if self.y < 128 - self.long_y:
            self.y += +1

class Aliment:
    def __init__(self):
        """ Un aliment est défini par un rayon égal à 3 et la position de son centre repéré par 
        son abscisse et son ordonnée attribuées aléatoirement:
        - son abscisse : nombre aléatoire entre les limites de la fenêtre de jeu sans dépasser!
        - son ordonnée: nombre aléatoire négatif de 0 à -400"""

        self.rayon = 3
        self.centre_x = randint(self.rayon,120-self.rayon)
        self.centre_y = -randint(0,400)

    def deplacer(self):
        """L'aliment se déplace verticalement, du haut vers le bas, avec une vitesse inférieure à celui du mobile.
        L'ordonnée de l'aliment est modifiée de 0.6"""
        self.centre_y = self.centre_y + 0.6

class Jeu:
    def __init__(self):
        """La classe Jeu crée les différents objets nécessaires au fonctionnement et à l'affichage du jeu.
        Trois attributs initialisés:
        - mobile : objet de la classe Mobile représentant le glouton
        - aliments : tableau contenant plusieurs objets de la classe Aliment représentant les différents aliments à gober par le glouton.
        - score : nombre entier associé aux aliments engloutis (+1) ou ratés (-1).
        """
        
        # Création de l'attribut glouton : objet de la classe Mobile
        self.glouton = Mobile()

        # création de l'attribut aliment : tableau d'objets de la classe Aliment
        self.aliments = [Aliment() for i in range(10)]

        # score réalisé au cours du jeu; nul au début
        self.score = 0

        # Initialisation de la fenêtre de jeu de taille 128x128 pixels à ne pas modifier !
        pyxel.init(128, 128, title="TP de jeu en POO")

        # Lancement du jeu à ne pas modifier !
        pyxel.run(self.update, self.draw)

    def mobile_deplacement(self):
        """déplacement avec les touches de directions:
        - si on appuie sur la touche -> on appelle la méthode deplacement_droite() de l'objet glouton (Mobile)
        - si on appuie sur la touche <- on appelle la méthode deplacement_gauche() de l'objet glouton (Mobile)
        - de même pour les déplacements haut et bas.
        """
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.glouton.deplacement_droite()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.glouton.deplacement_gauche()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.glouton.deplacement_bas()
        if pyxel.btn(pyxel.KEY_UP):
            self.glouton.deplacement_haut()

    def gerer_aliments(self):
        """Pour chaque aliment du tableau:
        1. on gère son déplacement de haut en bas,
        2. on gère son engloutissement par le glouton => le glouton grossit
        3. on gère sa sortie en bas d'écran => le glouton maigrit
        Dans les 2 cas, l'aliment est retiré du tableau des aliments.
        """
        for aliment in self.aliments:
            aliment.deplacer()
            if self.gober_aliment(aliment):
                self.glouton.grossir()
                self.aliments.remove(aliment)
                self.score += 1
            if self.rater_aliment(aliment):
                self.glouton.maigrir()
                self.score += -1
                self.aliments.remove(aliment)

    def afficher_aliments(self):
        """Affichage des aliments"""
        for aliment in self.aliments:
            pyxel.circ(aliment.centre_x,aliment.centre_y,aliment.rayon,3)

    def gober_aliment(self,aliment):
        """Le glouton attrape un aliment et le gobe.
        La fonction renvoie un booléen qui vérifie que le glouton est en position d'attraper l'aliment!"""

        return (self.glouton.x < aliment.centre_x < self.glouton.x + self.glouton.long_x) and  (self.glouton.y < aliment.centre_y < self.glouton.y + self.glouton.long_y)

    def rater_aliment(self,aliment):
        """Le glouton manque l'aliment et celui-ci arrive en bas de fenêtre.
        La fonction renvoie un booléen qui vérifie que l'aliment est en bas de fenêtre !"""

        if aliment.centre_y > 128:
            return True
        else:
            return False
        
    # =====================================================
    #                        UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du glout de la classe Mobile
        self.mobile_deplacement()

        # Gestion des aliments de la classe Aliment
        self.gerer_aliments()

    # =====================================================
    #                        DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        # représentation du glouton par une forme carrée (8 x 8)
        pyxel.rect(self.glouton.x, self.glouton.y, self.glouton.long_x, self.glouton.long_y, 2)
        
        # Représentation des aliments avec la méthode d'affichage dédiée.
        self.afficher_aliments()

if __name__ == '__main__':
    Jeu()