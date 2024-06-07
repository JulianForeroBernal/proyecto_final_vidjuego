import pygame as pg
import constantes as cons
pg.init()
pg.mixer.init()

sonido_moneda = pg.mixer.Sound("sonidos/coin.wav")
sonido_pocion = pg.mixer.Sound("sonidos/heal.wav")

class Items(pg.sprite.Sprite):
    def __init__(self,x,y,animacion_item,tipo_de_item):
        pg.sprite.Sprite.__init__(self)
        self.animacion_item = animacion_item
        self.index = 0
        self.image = self.animacion_item[self.index]
        self.rect = self.image.get_rect()
        self.update_time = pg.time.get_ticks()
        self.item_type = tipo_de_item
        self.rect.center = (x,y)
        self.contador = 1
    def update(self,jugador):
        if self.index >= len(self.animacion_item):
            self.index = 0
        if self.contador > 0 and self.contador < 10 :
            self.rect.y -= 1
            self.contador += 1
            if self.contador == 9 :
                self.contador = 19 
        if self.contador > 10 and self.contador < 20 :
            self.rect.y += 1
            self.contador -=1
            if self.contador == 11:
                self.contador = 1        
        self.image = self.animacion_item[self.index]
        if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
            self.index += 1
            self.update_time = 0
        if self.item_type == 1:
            if jugador.rect.colliderect(self.rect):
                sonido_moneda.play()
                self.kill()
                jugador.puntuacion += 25
        if self.item_type == 2 :
            if jugador.rect.colliderect(self.rect):
                sonido_pocion.play()
                self.kill()
                if jugador.vida < 99 :
                    jugador.vida += 25
        

        
        
    