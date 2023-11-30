import pyxel

def va_et_vient():
    global x,y,aller
    
    if aller:
        if x < 190:
            x = x + 1
        else:
            aller = False
    if not(aller):
        if x > 0:
            x = x - 1
        else:
            aller = True

def contourne():
    global x,y
    
    if x < 190 and y == 0:
        x = x + 1
    elif x == 190 and y < 90:
        y = y + 1
    elif x > 0 and y== 90:
        x = x - 1
    else:
        y = y - 1
        

x = 0
y = 0
aller=True

# Etats du jeu
def update():
    
    #va_et_vient()
    contourne()
    
# Dessin des états de jeu
def draw():
    pyxel.cls(0)
    pyxel.rect(x,y,10,10,3)
    

# taille de la fenetre 128x128 pixels
pyxel.init(200, 100, title="Projet jeu")

# Lancement de la boucle de jeu
pyxel.run(update,draw)