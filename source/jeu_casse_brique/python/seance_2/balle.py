import pyxel

hauteur_fenetre = 128
largeur_fenetre = 128
x = 64
y = 120
r = 2
dx = 1
dy = 1
pos = 48
long = 32
hauteur_raquette = 4


game_over = False
coef = 2
longueur_brique = 20
hauteur_brique = 4
hauteur_mur = 4*(1+hauteur_brique)+30
mur_brique = [(1+(1+longueur_brique)*i,20+(1+hauteur_brique)*j) for i in range(6) for j in range(4)]

def mouvement_balle(x,y):
    """
    Le centre (x,y) de la balle de rayon r doit rester dans la fenetre 128x128
    - un changement de direction horizontal signifie remplacer dx par -dx
    - un changement de direction vertical signifie remplacer dy par -dy
    """
    global dx,dy
    if (x <= r) or (x >= 128-r):
        dx = -dx
    if (y <= r) or (y >= 128-r):
        dy = -dy
    return x + dx, y + dy

def mouvement_raquette():
    global long,pos,largeur_fenetre
    
    if pyxel.btn(pyxel.KEY_RIGHT) and pos <= largeur_fenetre - long:
        pos += 5
    if pyxel.btn(pyxel.KEY_LEFT) and pos >= 0:
        pos -= 5
    return pos

def frappe_balle():
    global x,y,r,dx,dy,pos
    
    if pos <= x <= pos + long:    
        dy = -dy
        x,y = mouvement_balle(x,y)

def casse_brique():
    global x,y,r,dx,dy,longueur_brique,hauteur_brique
    
    for brique in mur_brique:
        if brique[0] <= x <= brique[0] + longueur_brique and (brique[1] <= y <= brique[1] + hauteur_brique):
            print(x,y,brique[1] + hauteur_brique)
            mur_brique.remove(brique)
            dy = -dy
            #x,y = mouvement_balle(x,y)
            
    
# Etats du jeu
def update():
    global x,y,r,dx,dy,pos,game_over
    x,y = mouvement_balle(x,y)
    pos = mouvement_raquette()
    # la balle touche le sol
    if y + r == hauteur_fenetre:
        game_over = True
    # la balle est au niveau de la raquette
    if y + r >= hauteur_fenetre - hauteur_raquette:
        frappe_balle()
    # la balle entre dans la zone du mur de briques.
    if y < hauteur_mur:
        casse_brique()
     

# Dessin des états de jeu
def draw():
    if not game_over:
        pyxel.cls(0)
        pyxel.circ(x*coef,y*coef,r*coef,10)
        pyxel.rect(pos*coef, (hauteur_fenetre-hauteur_raquette)*coef,long*coef,hauteur_raquette*coef,3)
        for brique in mur_brique:
            pyxel.rect(brique[0]*coef,brique[1]*coef,longueur_brique*coef,hauteur_brique*coef,4)
    else:
        pyxel.cls(0)
        pyxel.rect(pos*coef, (hauteur_fenetre-hauteur_raquette)*coef,long*coef,hauteur_raquette*coef,3)
        pyxel.text(20,50,"Perdu !",15)
    


# taille de la fenetre 128x128 pixels
pyxel.init(largeur_fenetre*coef, hauteur_fenetre*coef, title="Trajectoire de balle")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
