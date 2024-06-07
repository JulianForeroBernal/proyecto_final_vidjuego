import pygame as pg
import constantes as cons
import math

pg.init()
pg.mixer.init()

sonido_daño_enemigo = pg.mixer.Sound("sonidos/enemi.wav")
class Enemigo(pg.sprite.Sprite):
    def __init__ (self,imagen_quieto,imagen_enemigo,imagen_muerte,imagen_enemigo_ataque,imagen_enemigo_caminar, x, y):
        pg.sprite.Sprite.__init__(self)
        self.animacion_enemigo = imagen_enemigo
        self.animacion_muerte = imagen_muerte
        self.animacion_enemigo_ataque = imagen_enemigo_ataque
        self.animacion_enemigo_caminar = imagen_enemigo_caminar
        self.image = imagen_quieto
        self.update_time = pg.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.index = 0
        self.vida = 100
        self.vivo = True
        self.moviminto = False
        self.delta_x = 0
        self.delta_y = 0
        
    def update(self,jugador,lista_obstaculos):
        clipped_line = ()
        if self.index >= 7:
            self.index = 0
        self.image = self.animacion_enemigo[self.index]
        if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
            self.index +=1
            self.update_time = pg.time.get_ticks()
        if self.vida <= 0 :
            self.image = self.animacion_muerte[self.index]
            self.index +=1 
            self.vida = 0
            self.vivo = False
        
        if jugador.rect.colliderect(self.rect) and self.vivo == True and jugador.vivo == True:
            if self.index >= 7:
                self.index = 0
            self.image = self.animacion_enemigo_ataque[self.index]
            jugador.vida -= 2
            sonido_daño_enemigo.play()
            if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
                self.index +=1
                self.update_time = pg.time.get_ticks()
                
        linea_de_vision = ((self.rect.centerx,self.rect.centery),(jugador.rect.centerx,jugador.rect.centery))
        
        for obs in lista_obstaculos:
            if obs[1].clipline(linea_de_vision):
                clipped_line = obs[1].clipline(linea_de_vision)
                
        distancia = math.sqrt(((self.rect.centerx - jugador.rect.centerx)**2 )+ ((self.rect.centery - jugador.rect.centery)**2))
        
        if not clipped_line and distancia < cons.DISTANCIA_SEGUIMIENTO:
            if jugador.rect.centerx < self.rect.centerx and self.vivo == True:
                self.delta_x = -3
                self.rect.x -= cons.VELOCIDAD_ENEMIGO
                if self.index >= 7:
                    self.index = 0
                self.image = self.animacion_enemigo_caminar[self.index]
                if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
                    self.index +=1
                    self.update_time = pg.time.get_ticks()  
                    
            if jugador.rect.centery < self.rect.centery and self.vivo == True :
                self.delta_y = -3
                self.rect.y -= cons.VELOCIDAD_ENEMIGO
                if self.index >= 7:
                    self.index = 0
                self.image = self.animacion_enemigo_caminar[self.index]
                if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
                    self.index +=1
                    self.update_time = pg.time.get_ticks()     
            if jugador.rect.centery > self.rect.centery and self.vivo == True :
                self.delta_y = 3
                self.rect.y += cons.VELOCIDAD_ENEMIGO 
                if self.index >= 7:
                    self.index = 0
                self.image = self.animacion_enemigo_caminar[self.index]
                if pg.time.get_ticks() - self.update_time > cons.VELOCIDAD_ANIMACION :
                    self.index +=1
                    self.update_time = pg.time.get_ticks()                 
            for obstaculo in lista_obstaculos :
                if self.delta_x > 0 :
                    if obstaculo[1].colliderect(self.rect):
                        self.rect.left = obstaculo[1].right
                if self.delta_y < 0 :
                    if obstaculo[1].colliderect(self.rect):
                        self.rect.top = obstaculo[1].bottom
                if self.delta_y > 0:
                    if obstaculo[1].colliderect(self.rect):
                        self.rect.bottom = obstaculo[1].top
                
                
                
                
    def draw(self,interfaz):
        interfaz.blit(self.image,self.rect)

        