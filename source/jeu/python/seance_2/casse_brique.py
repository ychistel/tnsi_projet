import pyxel
from random import randint

class Mobile:
    
    def __init__(self):
        # Création du mobile
        self.x = 
        
      
    def mouvement(self):
        
                
class Jeu:
    
    def __init__(self):
        
        # constantes du jeu
        self.TITLE = "Casse brique"
        self.WIDTH = 128
        self.HEIGHT = 128
        self.CASE = 8
        
        self.FRAME_REFRESH = 10
        self.score = 0
        self.game_over = False
        
        # Création 
        
        # Lancement du jeu
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        pyxel.run(self.update,self.draw)

    def update(self):
        
            
            

    def draw(self):
        # écran : à effacer puis remplir de noir
        pyxel.cls(0)
        
        
        
        # affichage du score
        pyxel.text(4,4,f'SCORE:{self.score}',7)
        
        if self.game_over:
            pyxel.text(10,self.WIDTH//2,f'GAME OVER',7)    
        

        
    
Jeu()

