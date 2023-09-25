import pyxel

class Jeu:
    # constantes du jeu
    TITLE = "snake"
    WIDTH = 200
    HEIGHT = 160
    CASE = 10
    
    FRAME_REFRESH = 6
    
    def __init__(self):

        # taille de la fenetre 128x128 pixels
        pyxel.init(Jeu.WIDTH, Jeu.HEIGHT, title=Jeu.TITLE)
        
        # Création du serpent
        self.serpent = [[3,3],[2,3],[1,3]]
        self.direction = [1,0]
        
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.frame_count % Jeu.FRAME_REFRESH == 0:
            tete = [self.serpent[0][0] + self.direction[0],self.serpent[0][1] + self.direction[1]]
            self.serpent.insert(0,tete)
            self.serpent.pop(-1)
            
            if pyxel.btn(pyxel.KEY_RIGHT) and self.direction in ([0,1],[0,-1]):
                self.direction = [1,0]
            elif pyxel.btn(pyxel.KEY_LEFT) and self.direction in ([0,1],[0,-1]):
                self.direction = [-1,0]
            elif pyxel.btn(pyxel.KEY_UP) and self.direction in ([1,0],[-1,0]):
                self.direction = [0,-1]
            elif pyxel.btn(pyxel.KEY_DOWN) and self.direction in ([1,0],[-1,0]):
                self.direction = [0,1]
            
            

    def draw(self):
        # écran : à effacer puis remplir de noir
        pyxel.cls(0)
        
        # On représente le corps du serpent
        for anneau in self.serpent:
            x,y = anneau[0], anneau[1]
            pyxel.rect(x * Jeu.CASE, y * Jeu.CASE, Jeu.CASE, Jeu.CASE, 11)
        
        # On représente la tête du serpent
        x_tete, y_tete = self.serpent[0]
        pyxel.rect(x_tete*Jeu.CASE, y_tete*Jeu.CASE, Jeu.CASE, Jeu.CASE, 9)
        
    
Jeu()

