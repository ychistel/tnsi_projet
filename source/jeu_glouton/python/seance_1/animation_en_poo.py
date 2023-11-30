import pyxel


class Mobile:
    
    def __init__(self,x,y,largeur,hauteur,couleur):
        self.x = x
        self.y = y
        self.larg = largeur
        self.haut = hauteur
        self.color = couleur
        self.aller = True
        
    def va_et_vient(self):
        
        if self.aller:
            if self.x < 190:
                self.x = self.x + 1
            else:
                self.aller = False
        if not(self.aller):
            if self.x > 0:
                self.x = self.x - 1
            else:
                self.aller = True

    def contourne(self):
    
        if self.x < 190 and self.y == 0:
            self.x = self.x + 1
        elif self.x == 190 and self.y < 90:
            self.y = self.y + 1
        elif self.x > 0 and self.y== 90:
            self.x = self.x - 1
        else:
            self.y = self.y - 1
            
    def affiche(self):
        
        pyxel.rect(self.x,self.y,self.larg,self.haut,self.color)
        
class Jeu:
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        pyxel.init(200, 100, title="Projet jeu")
        
        # On crée un objet mobile car
        self.car_1 = Mobile(0,50,10,10,3)
        self.car_2 = Mobile(0,0,10,10,5)
        
        # Lancement de la boucle de jeu
        pyxel.run(self.update,self.draw)

    # Etats du jeu
    def update(self):
        self.car_1.va_et_vient()
        self.car_2.contourne()

    # Dessin des états du jeu
    def draw(self):
        pyxel.cls(0)
        self.car_1.affiche()
        self.car_2.affiche()
    
Jeu()