import pygame 
from person import Personaje

pygame.init() #metodo para inicializar pygame si no pues como monda va a funcionar

tamaño= (1300,700)
ventana = pygame.display.set_mode((tamaño)) #pa mostrar la ventana pa! esa monda traduce algo como pygame pantalla modo pa poner pantalla "pyg.pantalla.modo de ajuste"
# doble parantesis por que yes (por que dentro debe haber una tupla que tiene que ir en parentesis)
#la pantalla pues toca guardala en una variable xd por que aja todo tiene que estar en algun lao funciona si no pero pa 
#trabajar con la pantalla es mejor tenerla guardada en algun lado
pygame.display.set_caption("Aprendiendo pygame") # pa ponerle nombre a la ventana (traduce algo asi como pyg.pantalla.modo de captura o modo de nombre de juego, pa los compas)

def escalar_imag (imagen, escala): #esta funcion agarra la cada una de las imagenes y las escala a el valor necesario
    w = imagen.get_width() # w va a ser igual a la imagen que le pasemos como parametro.obtener_ancho()
    a = imagen.get_height() #a "                                                      ".obtener_alto()
    imagen_nueva = pygame.transform.scale(imagen, (w*escala , a*escala)) #la misma funcion de escalar
    return imagen_nueva

animation = [] # lista que tendra dentro cada una de las imagenes de la animacion de caminar del personaje

for i in range(10): #este for asigna a la lista animation todas las 10 imagenes del caminar del prota
    imag = pygame.image.load(f"imagenes/jugador/run_{i+1}.png") #imag = pygame.imagen.cargaresaimagen(f"direcionde la iamagen{i}")
    imag = escalar_imag(imag,2) # asiga a la misma variable la imagen ya escalada imag = funcion escalar imagen (la imagen xd, escala)
    animation.append(imag) #agrega a la lista de animacion cada imagen desde la carpeta y ya escalada
    
                    #YA NO SE USA PERO NO ES MALO RECORDARLO
                    
                    #player_image = pygame.image.load("imagenes/jugador/run_1.png") # en una variable de "imagen de jugador" se almacena la imagen con el comando
                    # pygame.image.load (osease: pygame.imagen.cargar la imagen ("que monda voa poner") :D )

                    #player_image = pygame.transform.scale(player_image, (player_image.get_width()*2,player_image.get_height()*2) ) #se modifica la varibale 
                    #player imagen con la funcion pygame.trasforma.a escala (que cosa se traforma, (parametros que se va a trasformar y por cuanto)) :)


player = Personaje(80,80, animation)
mover_derecha = False
mover_izquierda = False #variables para controlar el movimiento
mover_arriba = False
mover_abajo = False
clock = pygame.time.Clock() # se instsasia el objeto reloj desde pygame para controlar la tasa de fps

 #toca hace run while para que no se cierre insofacto la ventana 
run = True
while run: #la variable evento pues almacenara los eventos que pasen en el jueguito namas
    clock.tick(60)
    ventana.fill((0,0,0)) #llena constantemente la pantalla de color negro para que al haber un cambio lo anterior se borre
    delta_x = 0  # variables que inidican que tanto avanzara el cuadro; se ponen dentro del while por que tiene que cambiar en cada frame
    delta_y = 0
    if mover_arriba == True:
        delta_y = -5
    if mover_abajo == True:           # si la varibale que controla el movimineto es verdadera (osea se oprimio la tecla para moverse)
        delta_y = 5                  # entonces la variable delta que indicara cuanto se mueve aumentara o disminuira su valor 
    if mover_derecha == True:         # todo tiene mucha logica en realidad pa! >:|
        delta_x = 5
    if mover_izquierda == True:
        delta_x = -5
    player.move(delta_x,delta_y)
    
    player.update()
    
    player.draw(ventana)  

    for event in pygame.event.get(): # para cada evento que pase en el registro de pygame.event.get() (metodo para garrar los eventos)
         # osease por evento se refiere a cualquier accion dentro de la pagina sea un clic una tecla etc. 
        if event.type == pygame.QUIT : # si el tipo de evento sea cual sea es igual a un evento que cierra el juego (a eso se refiere pygame.QUIT 
             #con QUIT en grande) 
            run = False #tons run se vuelve falso y deja de funcionar el el ciclo osea se cierra la pagina  
        if event.type == pygame.KEYDOWN: # ahora vamos a hacer que el cuadrito en este caso se mueva segun que oprimimos
            if event.key == pygame.K_LEFT: 
                mover_izquierda = True     
            if event.key == pygame.K_RIGHT: #este me lo se no voy a comentar nada 
                mover_derecha = True           
            if event.key == pygame.K_DOWN: 
                mover_abajo = True
            if event.key == pygame.K_UP: 
                mover_arriba = True
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT:
                mover_derecha = False
            if event.key == pygame.K_DOWN:
                mover_abajo = False
            if event.key == pygame.K_UP:
                mover_arriba = False
                
        # :D
            
    
    pygame.display.update() # actualiza los cambios que se hacen como en este caso dibujar a cuadradito 
    #sino pues e queda en la parte de arriba donde creamos la ventana pero no hace mas, ahora con esta funcion agarra las
    #cosas nuevas que le dijimos que hiciera y pues la hace xd      
pygame.quit #esta funcion con quit chiquito es simplemente pa finalilzar pygame

#------------------------- hora si viene lo chido (toca ponerlo en el while xd) ------------------------------
