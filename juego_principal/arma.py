import pygame as pg
import constantes as cons
from bala import Bala


pg.init()
class Arma():
    def __init__(self, image, imagen_bala) :
        self.imagen_bala = imagen_bala
        self.imagen_originial = image
        self.angulo = 0
        self.imagen = pg.transform.rotate(self.imagen_originial, self.angulo)
        self.forma = self.imagen.get_rect()
        self.disparo = False
    def update(self,personaje):
        bala = None 
        self.forma.center = personaje.rect.center        
        self.forma.y += 15
        if personaje.direccion == "derecha":
            self.forma.x += personaje.shape.width / cons.DISTANCIA_ARMA
            self.forma.y += 10  
            self.rotar(False)  
        if personaje.direccion == "izquierda":
            self.forma.x -= personaje.shape.width / cons.DISTANCIA_ARMA
            self.forma.y += 10
            self.rotar(True)
        if pg.mouse.get_pressed()[0] and self.disparo == False:
            bala = Bala(self.imagen_bala, self.forma.centerx,self  .forma.centery)
            self.disparo = True
        if pg.mouse.get_pressed()[0]== False:
            self.disparo = False
        return bala
        
        
    def draw(self, interfaz):
        interfaz.blit(self.imagen, self.forma)
    def rotar(self, rotar):
        if rotar == True:
            imagen_rotada = pg.transform.flip(self.imagen_originial,True,False)
            self.imagen = pg.transform.rotate(imagen_rotada, self.angulo)
        else:
            imagen_rotada = pg.transform.flip(self.imagen_originial,False,False)
            self.imagen = pg.transform.rotate(imagen_rotada, self.angulo)