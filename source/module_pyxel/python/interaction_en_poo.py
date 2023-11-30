import pyxel

class Jeu:
    def __init__(self):
        
        self.LARGEUR = 128
        self.HAUTEUR = 128
        self.COTE = 4
        self.x = self.LARGEUR//2-self.COTE//2
        self.y = self.HAUTEUR//2-self.COTE//2
        # taille de la fenetre 128x128 pixels
        pyxel.init(self.LARGEUR, self.HAUTEUR, title="Projet jeu")

        # Lancement de la boucle de jeu
        pyxel.run(self.update,self.draw)

    # Etats du jeu
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < self.LARGEUR - self.COTE:
            self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < self.HAUTEUR - self.COTE:
            self.y = self.y + 1

    # Dessin des états du jeu
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x,self.y,self.COTE,self.COTE,8)
    
Jeu()