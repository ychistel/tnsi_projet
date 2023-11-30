import pyxel

class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        pyxel.init(128, 128, title="Projet jeu")

        # Lancement de la boucle de jeu
        pyxel.run(self.update,self.draw)

    # Etats du jeu
    def update(self):
        pass

    # Dessin des états du jeu
    def draw(self):
        pass
    
Jeu()

