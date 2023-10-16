import pyxel

x = 64
y = 4
r = 2
dx = 1
dy = 1
pos = 0
long = 32
haut = 4
coef = 5

def mouvement_balle(x,y):
    global dx,dy
    if x >= 128-r:
        dx = -1
    if x <= r:
        dx = 1
    if y >= 128-r:
        dy = -1
    if y<= r:
        dy = 1
    return x + dx, y + dy

def mouvement_raquette():
    global long,pos
    if pyxel.btn(pyxel.KEY_RIGHT) and pos <= 128 - long:
        pos += 1
    if pyxel.btn(pyxel.KEY_LEFT) and pos >= 0:
        pos -= 1
    return pos

# Etats du jeu
def update():
    global x,y,r,pos
    x,y = mouvement_balle(x,y)
    pos = mouvement_raquette()
    
        

# Dessin des états de jeu
def draw():
    pyxel.cls(0)
    pyxel.circ(x*coef,y*coef,r*coef,2)
    pyxel.rect(pos*coef, (128-haut)*coef,long*coef,haut*coef,3)
    


# taille de la fenetre 128x128 pixels
pyxel.init(128*coef, 128*coef, title="Trajectoire de balle")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
