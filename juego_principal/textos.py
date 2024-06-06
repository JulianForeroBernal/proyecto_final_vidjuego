import pygame as pg 
    
class TextoDaño(pg.sprite.Sprite):
    def __init__(self,x,y,texto,font,color):
        pg.sprite.Sprite.__init__(self)
        self.image = font.render(texto,True,color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.contador = 0
        
    def update(self):
        self.rect.y -= 3
        self.contador += 1 
        if self.contador > 24:
            self.kill() 
        