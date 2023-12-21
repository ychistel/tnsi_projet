import pyxel

hauteur_fenetre = 128
largeur_fenetre = 128
x = 64
y = 120
r = 2
dx = 1
dy = -1
pos = 48
long = 32
hauteur_raquette = 4

winner = False
game_on = False
game_over = False
coef = 1
"""
longueur_brique = 20
hauteur_brique = 4
espace = 10
hauteur_mur = 4*(1+hauteur_brique)+espace
mur_brique = [(1+(1+longueur_brique)*i,espace+(1+hauteur_brique)*j) for i in range(6) for j in range(4)]
"""
espace_mur = 20
longueur_brique = 19
hauteur_brique = 4
hauteur_mur = 20
mur_brique = [(5,20),(25,20),(45,20),(65,20),(85,20),(105,20), # ligne 1
              (5,25),(25,25),(45,25),(65,25),(85,25),(105,25), # ligne 2
              (5,30),(25,30),(45,30),(65,30),(85,30),(105,30), # ligne 3
              (5,35),(25,35),(45,35),(65,35),(85,35),(105,35)] # ligne 4

def mouvement_balle():
    """
    Le centre (x,y) de la balle de rayon r doit rester dans la fenetre 128x128
    - un changement de direction horizontal signifie remplacer dx par -dx
    - un changement de direction vertical signifie remplacer dy par -dy
    """
    global x,y,dx,dy
    if (x <= r) or (x >= 128-r):
        dx = -dx
    if (y <= r) or (y >= 128-r):
        dy = -dy
    # on modifie les coordonnées de la balle de dx et dy
    x,y = x+dx, y+dy

def mouvement_raquette():
    global long,pos,largeur_fenetre
    
    if pyxel.btn(pyxel.KEY_RIGHT) and pos <= largeur_fenetre - long:
        pos += 5
    if pyxel.btn(pyxel.KEY_LEFT) and pos >= 0:
        pos -= 5

def frappe_balle():
    global x,y,dx,dy,pos,long
    
    if y + r >= hauteur_fenetre - hauteur_raquette:
        if (pos <= x <= pos + long/3) and dx > 0:
            dy = -dy
            dx = -dx
        elif (pos + 2*long/3 < x <= pos + long) and dx < 0:
            dy = -dy
            dx = -dx
        else:
            dy = -dy

def casse_brique():
    global x,y,r,dx,dy,longueur_brique,hauteur_brique,winner
    
    if mur_brique == []:
        winner = True
    else:
        for brique in mur_brique:
            if (brique[0] <= x <= brique[0] + longueur_brique) and (brique[1] <= y <= brique[1] + hauteur_brique):
                mur_brique.remove(brique)
                dy = -dy
                  
# Etats du jeu
def update():
    global x,y,r,dx,dy,pos,game_on,game_over
    
    if game_on:
        # calcul de la position de la balle
        mouvement_balle()
        # calcul de la position de la raquette
        mouvement_raquette()
        # Gestion des collisions de la balle
        if y < hauteur_fenetre// 2:
            # la balle entre dans la zone du mur de briques.
            casse_brique()
        elif hauteur_fenetre // 2 <= y < hauteur_fenetre-r:
            # la balle est au niveau de la raquette
            frappe_balle() 
        else:
            # la balle touche le sol
            game_over = True
    else:
        # on déplace la raquette
        mouvement_raquette()
        # la balle suit le mouvement de la raquette donc on modifie x
        x = (pos + long/2)
        # on écoute l'événement de la touche ESPACE pour modifier la variable game_on
        if pyxel.btn(pyxel.KEY_SPACE):
            game_on = True
 
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
    if winner:
        pyxel.cls(0)
        pyxel.text(20,50,"GAGNE !",10)
    


# taille de la fenetre 128x128 pixels
pyxel.init(largeur_fenetre*coef, hauteur_fenetre*coef, title="Trajectoire de balle")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
