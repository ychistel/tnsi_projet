import pyxel
from random import randint

class Jeu:
    
    def __init__(self):
        
        # constantes du jeu
        self.TITLE = "snake"
        self.WIDTH = 128
        self.HEIGHT = 128
        self.CASE = 8
        
        self.FRAME_REFRESH = 15
        self.score = 0
        self.game_over = False
        # Création du serpent
        self.serpent = [[3,3],[2,3],[1,3]]
        self.direction = [1,0]
        
        # création d'une pomme
        self.pomme = [randint(1,self.WIDTH//self.CASE-1),randint(1,self.HEIGHT//self.CASE-1)]
        
        # Lancement du jeu
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        pyxel.run(self.update,self.draw)

    def update(self):
        if pyxel.frame_count % self.FRAME_REFRESH == 0 and not self.game_over:
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
            
            # test si le serpent sort du cadre de jeu ou se mord
            if (tete in self.serpent[1:]) \
               or (tete[0] > self.WIDTH/self.CASE - 1) \
               or (tete[0] < 0)\
               or (tete[1] > self.HEIGHT/self.CASE - 1)\
               or (tete[1] < 0):
                
                self.game_over = True;
            
            # test si le serpent mange la pomme
            if (tete == self.pomme):
                self.pomme = [randint(1,self.WIDTH//self.CASE-1),randint(1,self.HEIGHT//self.CASE-1)]
                tete = [self.serpent[0][0] + self.direction[0],self.serpent[0][1] + self.direction[1]]
                self.serpent.insert(0,tete)
                self.score += 1
            

    def draw(self):
        # écran : à effacer puis remplir de noir
        pyxel.cls(0)
        
        # On représente le corps du serpent
        for anneau in self.serpent:
            x,y = anneau[0], anneau[1]
            pyxel.rect(x * self.CASE, y * self.CASE, self.CASE, self.CASE, 11)
        
        # On représente la tête du serpent
        x,y = self.serpent[0]
        pyxel.rect(x*self.CASE, y*self.CASE, self.CASE, self.CASE, 9)
        
        # on représente la pomme
        x,y = self.pomme
        print(x,y)
        pyxel.rect(x*self.CASE, y*self.CASE, self.CASE, self.CASE, 8)
        
        # affichage du score
        pyxel.text(4,4,f'SCORE:{self.score}',7)
        
        if self.game_over:
            pyxel.text(10,self.WIDTH//2,f'GAME OVER',7)    
        
    
Jeu()

