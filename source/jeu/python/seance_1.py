import pyxel

class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        pyxel.init(128, 128, title="Projet jeu")

        pyxel.run(self.update,self.draw)

    def update(self):
        pass

    def draw(self):
        pass
    
Jeu()

