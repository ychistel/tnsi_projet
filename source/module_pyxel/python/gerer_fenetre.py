import pyxel

# Etats du jeu
def update():
    pass

# Dessin des états de jeu
def draw():
    pyxel.rect(0,0,10,10,1)
    pyxel.rect(160,0,20,20,2)
    pyxel.rect(150,70,30,30,3)
    pyxel.rect(0,60,40,40,4)


# taille de la fenetre 128x128 pixels
pyxel.init(180, 100, title="Première fenêtre")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
