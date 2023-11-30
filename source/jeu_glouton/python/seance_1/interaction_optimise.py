import pyxel

LARGEUR = 128
HAUTEUR = 128
COTE = 4
x = LARGEUR//2-COTE//2
y = HAUTEUR//2-COTE//2

# Etats du jeu
def update():
    global x,y
    
    if pyxel.btn(pyxel.KEY_RIGHT) and x < LARGEUR - COTE:
        x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x = x - 1
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y = y - 1
    if pyxel.btn(pyxel.KEY_DOWN) and y < HAUTEUR - COTE:
        y = y + 1

# Dessin des états de jeu
def draw():
    pyxel.cls(0)
    pyxel.rect(x,y,COTE,COTE,8)


# taille de la fenetre 128x128 pixels
pyxel.init(LARGEUR, HAUTEUR, title="Première interaction")

# Lancement de la boucle de jeu
pyxel.run(update,draw)