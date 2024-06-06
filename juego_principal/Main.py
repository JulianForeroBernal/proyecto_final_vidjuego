import pygame as pg
import sys
import constantes as cons
from personaje import Personaje
from arma import Arma
from enemigos import Enemigo
from textos import TextoDaño
from items import Items

pg.init() #inicializador de pygame

#AJUSTES VENTANA 
ventana = pg.display.set_mode((cons.ANCHO,cons.ALTO))
fondo = pg.image.load("imagenes/ambiente/mapa.jpg")
fondo = pg.transform.scale(fondo.convert(),(cons.ANCHO,cons.ALTO))
pg.display.set_caption("DOCE PODEROSOS FPS")

#FUNCION PARA DIBUJAR TEXTOS 
def dibujar_textos(texto,font,color,x,y):
    img = font.render(texto,True,color)
    ventana.blit(img,(x,y))

#DECLARACION DE VARIABLES PARA CONTROL DEL CICLO
clock = pg.time.Clock() # variable reloj para el control de fps

#FUENTES
fuente = pg.font.Font("imagenes/fuentes/fuente.ttf", 20) 
grupo_sprites_textos = pg.sprite.Group()

#imagenes corazones
corazon_lleno = pg.image.load("imagenes/jugador/items/corazon_lleno.png")
corazon_lleno = pg.transform.scale(corazon_lleno,(corazon_lleno.get_width()*cons.ESCALA_CORAZONES, corazon_lleno.get_height()*cons.ESCALA_CORAZONES))
corazon_vacio = pg.image.load("imagenes/jugador/items/corazon_vacio.png")
corazon_vacio = pg.transform.scale(corazon_vacio,(corazon_vacio.get_width()*cons.ESCALA_CORAZONES, corazon_vacio.get_height()*cons.ESCALA_CORAZONES))

#instancias jugador
jugador = Personaje((200,200))  #instancia personaje
grupo_sprites_player = pg.sprite.Group()
grupo_sprites_player.add(jugador)
def corazones_jugador():
    for i in range (0,4):
        if jugador.vida >= ((i+1)*25):
            ventana.blit(corazon_lleno,(20+i*50,25))
        elif jugador.vida % 25 > 0 :
            ventana.blit(corazon_vacio,(20+i*50,25))


#instansia arma
imagen_arma = pg.image.load("imagenes/jugador/arma.png")
imagen_arma= pg.transform.scale(imagen_arma,(imagen_arma.get_width()*0.7, imagen_arma.get_height()*0.7))
cont_seg = pg.time.Clock()
#instancias bala
imagen_bala = pg.image.load("imagenes/jugador/bala.png")
arma = Arma(imagen_arma,imagen_bala) 
grupo_sprites_balas = pg.sprite.Group()

#AJUSTES INICIALES ENEMIGOS
imagen_enemigo = []
imagen_enemigo_caminar = []
imagen_enemigo_muerte = []
imagen_enemigo_ataque = []
imagen_quieto_enemigo_1 = pg.image.load("imagenes/enemigos/negro_chiquito_1.png")
imagen_quieto_enemigo_1 = pg.transform.scale(imagen_quieto_enemigo_1,(imagen_quieto_enemigo_1.get_width()*2.5, imagen_quieto_enemigo_1.get_height()*2.5))
for i in range (0,8):
    aux_imagen = pg.image.load(f"imagenes/enemigos/negro_chiquito_{i+1}.png")
    aux_imagen = pg.transform.scale(aux_imagen,(aux_imagen.get_width()*2.5, aux_imagen.get_height()*2.5))
    imagen_enemigo.append(aux_imagen)
for j in range (0,8):
    aux_imagen_2 = pg.image.load(f"imagenes/enemigos/sheet_caminar_{j+1}.png")
    aux_imagen_2 = pg.transform.scale(aux_imagen_2,(aux_imagen_2.get_width()*2.5, aux_imagen_2.get_height()*2.5))
    imagen_enemigo_caminar.append(aux_imagen_2)
for k in range (0,8):
    aux_imagen_3 = pg.image.load(f"imagenes/enemigos/sheet_muerte_{i+1}.png")
    aux_imagen_3 = pg.transform.scale(aux_imagen_3,(aux_imagen_3.get_width()*2.5, aux_imagen_3.get_height()*2.5))
    imagen_enemigo_muerte.append(aux_imagen_3)
for l in range (0,8):
    aux_imagen_4 = pg.image.load(f"imagenes/enemigos/sheet_ataque_{l+1}.png")
    aux_imagen_4 = pg.transform.scale(aux_imagen_4,(aux_imagen_4.get_width()*2.5, aux_imagen_4.get_height()*2.5))
    imagen_enemigo_ataque.append(aux_imagen_4) 
enemigo = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,1000,225)
enemigo_2 = Enemigo(imagen_quieto_enemigo_1,imagen_enemigo,imagen_enemigo_muerte,imagen_enemigo_ataque,1000,640)
lista_enemigos = [enemigo,enemigo_2]

#AJUTES INICIALELS ITEMS 
sheet_coin = pg.image.load("imagenes/jugador/items/coin_.png")
animacion_moneda = []
for i in range (0,11):
    animacion_aux = pg.Rect(cons.PIXELES_FRAME_MONEDA*i,0,cons.PIXELES_FRAME_MONEDA,cons.PIXELES_FRAME_MONEDA)
    animacion_moneda.append(sheet_coin.subsurface(animacion_aux))

animacion_pocion = pg.image.load("imagenes\jugador\items\pocion.png")
animacion_pocion = pg.transform.scale(animacion_pocion,(animacion_pocion.get_width()*0.5,animacion_pocion.get_height()*0.5),)

coi_1 = Items(100,100,animacion_moneda,1)
poscion_1 = Items (100,200,[animacion_pocion],2)

grupo_sprites_items = pg.sprite.Group()
grupo_sprites_items.add(coi_1)
grupo_sprites_items.add(poscion_1)

#CICLO DE JUEGO
run = True


while run:

    clock.tick(cons.FPS) #control fps
    ventana.fill(cons.NEGRO)
    ventana.blit(fondo,(0,0))
    pg.display.update()
    
    #UPDATES
    print(jugador.puntuacion)
    #update jugador
    grupo_sprites_player.update(lista_enemigos)
    corazones_jugador()    #dibujar corazones
    key = pg.key.get_pressed()
    jugador.control_tecla(key)
    #update balas
    bala = arma.update(jugador)
    if bala:
        grupo_sprites_balas.add(bala)
    for bala in grupo_sprites_balas:
        damage , pos_daño = bala.update(lista_enemigos,jugador)
        if damage != 0:
            daño_texto = TextoDaño(pos_daño.centerx,pos_daño.centery,str(damage),fuente,cons.ROJO)
            grupo_sprites_textos.add(daño_texto)  
              
    #update enemigos   
    for enemi in lista_enemigos:
        enemi.update(jugador)
        enemi.draw(ventana)
        
    #update items
    grupo_sprites_items.update(jugador)
    
    #update textos
    grupo_sprites_textos.update()
    dibujar_textos(f"Puntuacion: {jugador.puntuacion}",fuente,cons.AMARILLO,1000,50)
    #DRAW´S    
    
    #dibujar jugador        
    grupo_sprites_player.draw(ventana)

    #dibujar el arma
    arma.draw(ventana)
    
    #dibujar balas
    grupo_sprites_balas.draw(ventana)
    
    #dibujar textos
    grupo_sprites_textos.draw(ventana)
    
    #dibujar items
    grupo_sprites_items.draw(ventana)
        
    #VENTANA    
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False         
            
pg.quit()
sys.exit()