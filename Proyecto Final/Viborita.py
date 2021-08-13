import turtle
import time
import random

posponer = 0.1 
aumento = []
score = 0
high_score = 0

#Funciones
def arriba():
    cserp.direction = "up"
def abajo():
    cserp.direction = "down"
def izquierda():
    cserp.direction = "left"
def derecha():
    cserp.direction = "right"
    
def mov():
    if cserp.direction == "up": #función para mover hacia arriba
        y = cserp.ycor() #definimos la variable y como la el eje y 
        cserp.sety(y + 20) #el movimiento será de 20 pixeles hacia arriba
    if cserp.direction == "down": #función para mover hacia abajo
        y = cserp.ycor() #definimos la variable y como la el eje y 
        cserp.sety(y - 20) #el movimiento será de 20 pixeles hacia abajo
    if cserp.direction == "left": #función para mover hacia izquierda
        x = cserp.xcor() #definimos la variable x como la el eje x 
        cserp.setx(x - 20) #el movimiento será de 20 pixeles hacia la izquierda
    if cserp.direction == "right": #función para mover hacia la derecha
        x = cserp.xcor() #definimos la variable x como la el eje x 
        cserp.setx(x + 20) #el movimiento será de 20 pixeles hacia la derecha

#Personalizar la Pantalla
pantalla = turtle.Screen() #Abrimos una ventana
pantalla.title("Bienvenido a mi juego de Snake") #Título de la ventana
pantalla.bgcolor("cyan") #color de la ventana
pantalla.setup(width =600, height=600) #Dimensiones de la ventana
pantalla.tracer(0) #Mejorar la animación 

#Marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0        High Score: 0", align = "center", font =("Courier", 24, "normal"))

#teclado
pantalla.listen() #decirle al programa que esté preparado para las indicaciones
pantalla.onkeypress(arriba, "Up") #Movimiento con las flechas del teclado
pantalla.onkeypress(abajo, "Down") #Movimiento con las flechas del teclado
pantalla.onkeypress(izquierda, "Left") #Movimiento con las flechas del teclado
pantalla.onkeypress(derecha, "Right") #Movimiento con las flechas del teclado


#Creación de la cabeza de la serpiente
cserp = turtle.Turtle()#Definimos un objeto
cserp.speed(0)#Mostramos la cabeza sin movimiento
cserp.shape("square")#Definimos la forma de la cabeza
cserp.color("green") #Color de la cabeza
cserp.penup() #Funcion para que la cabeza no deje rastro al avanzar 
cserp.goto(0,0)#Posición inicial de la cabeza en mi plano
cserp.direction="stop"#Cabeza en reposo en las coordenadas (0,0)

#Creación de las manzanas
manzana = turtle.Turtle()#Definimos un objeto
manzana.speed(0)#Mostramos la comida sin movimiento
manzana.shape("circle")#Definimos la forma de la comida
manzana.color("red") #Color de la comida
manzana.penup() #Funcion para que la comida no deje rastro al avanzar 
manzana.goto(0,200)#Posición inicial de la comida en mi plano

while True:
    pantalla.update() #actualizamos constantemente la pantalla
    
    if cserp.xcor() > 280 or cserp.xcor() < -280 or cserp.ycor() > 280 or cserp.ycor() < -280: #se genera un límite en los bordes para que la serpiente no pueda pasar
        time.sleep(1) #si choca con los bordes se pone un tiempo de 1 segundo
        cserp.goto(0,0) #la cabeza regresa a la posición inicial
        cserp.direction = "stop" #no hay movimiento
        for cuerpo in aumento:
            cuerpo.goto(1000,1000) #El cuerpo se va lejos de la pantalla
        aumento.clear() #Se borra el progreso que teníamos en el cuerpo
        score = 0
        texto.clear()
        texto.write(" Score: {}      High Score: {} ".format(score, high_score), align = "center", font =("Courier", 24, "normal")) #formato
    
    if cserp.distance(manzana) < 20: #si la distancia es menor a 20 pixeles entre la serpiente y las manzanas 
        x = random.randint(-280,280) #posición de las manzanas aleatorias entre esas coordenadas
        y = random.randint(-280,280) #posición de las manzanas aleatorias entre esas coordenadas
        manzana.goto(x,y) #posición de las manzanas aleatorias entre esas coordenadas
        
        cuerpo = turtle.Turtle()
        cuerpo.speed(0)
        cuerpo.shape("square")
        cuerpo.color("green") 
        cuerpo.penup() 
        aumento.append(cuerpo)
        
        score += 10 #Aumentamos en 10 puntos el score
        
        if score > high_score:
            high_score = score #si nuestro score es mayor al high_score actualizamos high_score
        texto.clear()
        texto.write(" Score: {}      High Score: {} ".format(score, high_score), align = "center", font =("Courier", 24, "normal")) #formato
        
    totcuerpo = len(aumento)
    for i in range(totcuerpo -1, 0, -1):
        x = aumento[i - 1].xcor()
        y = aumento[i - 1].ycor()
        aumento[i].goto(x,y)
        
    if totcuerpo > 0:
        x = cserp.xcor()
        y = cserp.ycor()
        aumento[0].goto(x,y)
      
                 
    
    mov() #llamamos a la función 
    
    for cuerpo in aumento:
        if cuerpo.distance(cserp) < 20: #Condición para ver si la cabeza choca con el cuerpo
            time.sleep(1) #1 segundo de espera
            cserp.goto(0,0) #cabeza regresa a la posición inicial
            cserp.direction = "stop" #la cabeza se encuentra sin moverse
            
            for cuerpo in aumento:  
                cuerpo.goto(1000,1000) #se mueve el cuerpo acumulado 
            aumento.clear() #se elimina el progreso
            score = 0
            texto.clear()
            texto.write(" Score: {}      High Score: {} ".format(score, high_score), align = "center", font =("Courier", 24, "normal")) #formato
    time.sleep(posponer) #delay para ver el movimiento






















turtle.exitonclick() #Comando para que no se cierre la ventana