import pyxel

# Etats du jeu
def update():
    global x
    
    if x < 128:
        x = x + 1
    else:
        x = 0

# Dessin des états de jeu
def draw():
    pyxel.cls(0)
    pyxel.rect(x,50,10,10,1)
    
x = 0

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128, title="Projet jeu")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
