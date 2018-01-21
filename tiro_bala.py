#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------
#---Autor: Rodrigo Barba G.
#---Fecha: 10-Ago-2017
#---correo: lrbarba@utpl.edu.ec
#--------------------

#---Simulador TIRO de BALA

import numpy as np
import cv2
import sys
import math

#Funciones
""" ----FUNCIONES MATEMÁTICAS-----------"""
def V_inicial_y(Velocidad,grados):
    return Velocidad*math.sin(math.radians(grados))

def V_inicial_x(Velocidad,grados):
    return Velocidad*math.cos(math.radians(grados))

def x_valor(Velocidad_x,tiempo):
    return Velocidad_x * tiempo

def y_valor(Altura, Velocidad_y, tiempo, gravedad):
    return Altura + (Velocidad_y*tiempo) - ((0.5)*gravedad*tiempo*tiempo)

def Vx(Velocidad_x):
    return Velocidad_x

def Vy(Velocidad_y, gravedad, tiempo):
    return Velocidad_y - (gravedad*tiempo)

def Alcance_maximo(Altura, Velocidad, angulo, gravedad):
    if Altura == 0:
        return (((Velocidad*Velocidad)*math.sin(math.radians(2*angulo)))/gravedad)
    else:
        z = (gravedad*Altura)/(Velocidad*Velocidad)
        return ((Velocidad*Velocidad)/gravedad)*(math.sin(math.radians(angulo))+math.sqrt(math.pow(math.sin(math.radians(angulo)),2)+(2*z)))*math.cos(math.radians(angulo))

def Altura_maxima(Altura, Velocidad, angulo, gravedad):
    if Altura == 0:
        return (Velocidad*Velocidad*math.pow(math.sin(math.radians(angulo)),2))/(2*gravedad)
    else:
        return (Velocidad*Velocidad*math.pow(math.sin(math.radians(angulo)),2))/(2*gravedad)+Altura

def Tiempo_vuelo(Altura, Velocidad, angulo, gravedad):
    if Altura == 0:
        return (2*Velocidad*math.sin(math.radians(angulo)))/(gravedad)
    else:
        z = (gravedad*Altura)/(Velocidad*Velocidad)
        return (Velocidad/gravedad)*(math.sin(math.radians(angulo))+(math.sqrt(math.pow(math.sin(math.radians(angulo)),2)+(2*z))))


""" ----------------------------"""
" distancia entre dos puntos del plano cartesiano"
def distancia(x1,y1,x2,y2):
    """ Devuelve la distancia entre ambos puntos. """
    dx = x2 - x1
    dy = y2 - y1
    return (dx*dx + dy*dy)**0.5

#Captura de video
video_capture = cv2.VideoCapture(0)

"--------Variables de trabajo--------"
ancho = int(video_capture.get(3))   # float
alto = int(video_capture.get(4)) # float
contador = 1; #variable para controlar el tiempo en segundos
tiempo = 0 #s
x_, y_ = int(0.1*ancho), int(0.66*alto) #Escala del plano cartesiano
Velocidad_y = 0  #Variable que valida direccion de las flechas
lista_x = [] #variable para almacenar la posicion en x
lista_y = [] #variable para almacenar la posicion en y
theta = 0 # angulo para dibujar la trayectoria de v
longitud = 50 # longitud del vector v
p2_x, p2_y = 0, 0 # Punto dos para dibujar el vector v

"-----------------------------------"
"--------Datos de simulacion--------"
"-----------------------------------"
#datos de que deben ingresar para realizar la simulacion
h = 20 #altura metros 0 a 50
Vo= 20  #velocidad inicial m/s 10 y 30
angulo = 45 #angulo en grados entre 0 y 90
gravedad = 9.8 #9.8m/s
"-----------------------------------"
"-----------------------------------"

#Calcular Vx_inicial, Vy_inicial,
aux_Vox = V_inicial_x(Vo,angulo)
aux_Voy = V_inicial_y(Vo,angulo)

#Calcular Vx = Vox
aux_Vx = Vx(aux_Vox)
aux_Vy = aux_Voy - gravedad * tiempo

#Graficar plano
escalay = distancia(int(0.1*ancho),int(0.66*alto),int(0.1*ancho),int(0.33*alto)) # eje y
escalax = distancia(int(0.1*ancho),int(0.66*alto),int(0.9*ancho),int(0.66*alto)) # eje x

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frameClone = frame.copy()
    contador = contador + 1
    font = cv2.FONT_HERSHEY_SIMPLEX

    #print distancia(int(0.1*ancho),int(0.66*alto),int(0.1*ancho),int(0.33*alto))
    #Escala de coordenadas del plano cartesiano
    "--------EJE  X----------"
    cv2.line(frameClone,(int(0.1*ancho),int(0.66*alto)),(int((0.9)*ancho),int(0.66*alto)),(0,0,255),2) #eje x
    cv2.circle(frameClone,(int(0.1*ancho)+int(0.2*escalax),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'20',(int(0.1*ancho)+int(0.2*escalax),int(0.66*alto)+int(0.1*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho)+int(0.4*escalax),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'40',(int(0.1*ancho)+int(0.4*escalax),int(0.66*alto)+int(0.1*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho)+int(0.6*escalax),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'60',(int(0.1*ancho)+int(0.6*escalax),int(0.66*alto)+int(0.1*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho)+int(0.8*escalax),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'80',(int(0.1*ancho)+int(0.8*escalax),int(0.66*alto)+int(0.1*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho)+int(1.0*escalax),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'100  m',(int(0.1*ancho)+int(1.0*escalax),int(0.66*alto)+int(0.1*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)

    "--------EJE  Y----------"
    cv2.line(frameClone,(int(0.1*ancho),int(0.33*alto)),(int((0.1)*ancho),int(0.66*alto)),(0,0,255),2) #eje y
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)),5,(255,0,0),-1)
    cv2.putText(frameClone,'0',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)-int(0.2*escalay)),5,(255,0,0),-1)
    cv2.putText(frameClone,'20',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)-int(0.2*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)-int(0.4*escalay)),5,(255,0,0),-1)
    cv2.putText(frameClone,'40',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)-int(0.4*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)-int(0.6*escalay)),5,(255,0,0),-1)
    cv2.putText(frameClone,'60',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)-int(0.6*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)-int(0.8*escalay)),5,(255,0,0),-1)
    cv2.putText(frameClone,'80',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)-int(0.8*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.circle(frameClone,(int(0.1*ancho),int(0.66*alto)-int(1.0*escalay)),5,(255,0,0),-1)
    cv2.putText(frameClone,'100  m',(int(0.1*ancho)-int(0.1*escalay),int(0.66*alto)-int(1.0*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)

    "-----Altura H------------"
    if h > 0:
        cv2.line(frameClone,(int(0.1*ancho),int(0.66*alto)-int((h/float(100))*escalay)),(int((0.9)*ancho),int(0.66*alto)-int((h/float(100))*escalay)),(0,255,255),1) #eje x
        cv2.line(frameClone,(int(0.04*ancho),int(0.66*alto)-int((h/float(100))*escalay)),(int((0.05)*ancho),int(0.66*alto)-int((h/float(100))*escalay)),(0,255,255),1) #barra arriba
        cv2.line(frameClone,(int(0.04*ancho), int(0.66*alto)), (int((0.05)*ancho),int(0.66*alto)),(0,255,255),1) #barra abajo
        cv2.line(frameClone,(int(0.045*ancho),int(0.66*alto)), (int((0.045)*ancho),int(0.66*alto)-int((h/float(100))*escalay)),(0,255,255),2) #barra vertical
        cv2.putText(frameClone,'H',(int(0.04*ancho)-int(0.1*escalay), int(int(0.66*alto)-int((h/float(100))*escalay)/2)), font, 0.5,(255,255,255),2,cv2.LINE_AA) # valor de la altura H

    "-----Texto para presentar datos--------"
    cv2.putText(frameClone,'Tiempo',(int(0.1*ancho),int(0.66*alto)-int(1.2*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Vx',(int(0.1*ancho),int(0.66*alto)-int(1.4*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Vy',(int(0.1*ancho),int(0.66*alto)-int(1.6*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, 'Vo',(int(0.3*ancho),int(0.66*alto)-int(1.4*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, 'Angulo',(int(0.3*ancho),int(0.66*alto)-int(1.6*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Altura Max',(int(0.3*ancho),int(0.66*alto)-int(1.2*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Altura H',(int(0.7*ancho),int(0.66*alto)-int(1.6*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Alcance Max',(int(0.7*ancho),int(0.66*alto)-int(1.4*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone,'Tiempo de vuelo',(int(0.7*ancho),int(0.66*alto)-int(1.2*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)

    cv2.putText(frameClone, "%.1f m/s" % (Vo),(int(0.3*ancho)+30,int(0.66*alto)-int(1.4*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, "%.1f grados" % (angulo),(int(0.3*ancho)+60,int(0.66*alto)-int(1.6*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, "%.2f m" % (h),(int(0.7*ancho)+150,int(0.66*alto)-int(1.6*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, "%.2f m" % Altura_maxima(h,Vo,angulo,gravedad),(int(0.3*ancho)+90,int(0.66*alto)-int(1.2*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, "%.2f m" % Alcance_maximo(h,Vo,angulo,gravedad),(int(0.7*ancho)+150,int(0.66*alto)-int(1.4*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(frameClone, "%.2f s" % Tiempo_vuelo(h,Vo,angulo,gravedad),(int(0.7*ancho)+150,int(0.66*alto)-int(1.2*escalay)), font, 0.5,(0,255,255),2,cv2.LINE_AA)

    "-----Alcance maximo------------"
    cv2.line(frameClone,(int(0.1*ancho),int(0.66*alto)+int(0.2*escalay)),(int(0.1*ancho)+int((Alcance_maximo(h,Vo,angulo,gravedad)/float(100))*escalax) ,int(0.66*alto)+int(0.2*escalay)),(0,255,255),1) #eje x
    cv2.line(frameClone,(int(0.1*ancho),int(0.03*alto)+int(2.0*escalay)),(int(0.1*ancho),int(0.09*alto)+int(2.0*escalay)),(0,255,255),1) #barra vertical inicio
    cv2.line(frameClone,(int(0.1*ancho)+int((Alcance_maximo(h,Vo,angulo,gravedad)/float(100))*escalax),int(0.03*alto)+int(2.0*escalay)),(int(0.1*ancho)+int((Alcance_maximo(h,Vo,angulo,gravedad)/float(100))*escalax),int(0.09*alto)+int(2.0*escalay)),(0,255,255),1) #barra vertical final
    cv2.circle(frameClone,(int(0.1*ancho)+int((Alcance_maximo(h,Vo,angulo,gravedad)/float(100))*escalax),int(0.66*alto)),5,(255,255,0),-1) # Circulo en el Eje X donde cae el proyectil
    cv2.putText(frameClone,'Alcance maximo',(int(((Alcance_maximo(h,Vo,angulo,gravedad)/float(100))*escalax)/2),int(0.66*alto)+int(0.3*escalay)), font, 0.5,(255,255,255),2,cv2.LINE_AA)

    "-----Tiempo de la bala---------"#Control de tiempo de bala""
    if (contador%10)==0:
        tiempo = tiempo + 0.1

        #Velocidad_y
        Velocidad_y = Vy(Vo,gravedad,tiempo)

        #Calcular los coordenadas (x,y)
        x_ = int(x_valor(aux_Vx,tiempo)) #* escala para x
        y_ = int(y_valor(h,aux_Voy,tiempo,gravedad)) #* escala para y

        # Colocar la posicion (x,y) del proyectil de acuerdo a la escala
        x_ = int((x_*escalax)/100) + int(0.1*ancho) # posicion x
        y_ = int(0.66*alto) - int((y_*escalay)/100) # posicion y

        #Angulo theta
        theta = math.degrees(math.atan((Velocidad_y/aux_Vx)))

        #Calcular las coordenadas (p2_x,p2_y) del vector v
        p2_x = int(x_ + longitud * math.cos(math.radians(theta)))
        p2_y = int(y_ + longitud * math.sin(math.radians(theta)))

        #guardar valores de coordenas del proyectil
        lista_x.append(x_)
        lista_y.append(y_)

    #dibujar proyectil y vectores de direccion del proyectil
    "-----Dibujar movimiento del proyectil, y los vectores Vx, Vy y V ------------"
    for i in range(x_, int((0.9)*ancho)):
        cv2.circle(frameClone,(x_, y_), 10, (0,0,255), -1)
        cv2.arrowedLine(frameClone, (x_, y_), (x_+80, y_), (255, 100, 100), 1, cv2.LINE_AA,0,0.2) # flecha vector Vx
        cv2.putText(frameClone,'Vx',(x_+80, y_), font, 0.5,(255,255,255),1,cv2.LINE_AA) # Texto Vx

        # visualizar variables de tiempo, Vx y Vy
        cv2.putText(frameClone, "%.1f s" % (tiempo),(int(0.1*ancho)+60,int(0.66*alto)-int(1.2*escalay)), font, 0.5,(0,255,255),1,cv2.LINE_AA)
        cv2.putText(frameClone, "%.2f m/s" % (Velocidad_y),(int(0.1*ancho)+60,int(0.66*alto)-int(1.4*escalay)), font, 0.5,(0,255,255),1,cv2.LINE_AA)
        cv2.putText(frameClone, "%.2f m/s" % (aux_Vx),(int(0.1*ancho)+60,int(0.66*alto)-int(1.6*escalay)), font, 0.5,(0,255,255),1,cv2.LINE_AA)

        "------Dibujar los vectores Vx, Vy y V -----------"
        if (tiempo>0):
            if (Velocidad_y > 0 ):
                cv2.arrowedLine(frameClone, (x_, y_), (x_, y_-80), (255, 100, 100), 1, cv2.LINE_AA,0,0.2) # flecha vector Vy
                cv2.putText(frameClone,'Vy',(x_, y_-80), font, 0.5,(255,255,255),1,cv2.LINE_AA) #Texto Vy
                #cv2.arrowedLine(frameClone, (x_, y_), (x_+ int(p2_x*0.5), int(2*y_ - p2_y)), (255, 100, 100), 1, cv2.LINE_AA,0,0.1) # vector V
                cv2.arrowedLine(frameClone, (x_, y_), (x_+ int(p2_x*0.2), int(2*y_ - p2_y)), (255, 100, 100), 1, cv2.LINE_AA,0,0.1) # vector V
                cv2.putText(frameClone,'V',(x_+ int(p2_x*0.2), int(2*y_ - p2_y)), font, 0.5,(255,255,255),1,cv2.LINE_AA) #Texto V
            else:
                cv2.arrowedLine(frameClone, (x_, y_), (x_, y_+80), (255, 100, 100), 1, cv2.LINE_AA,0,0.2) # flecha vector Vy
                cv2.putText(frameClone,'Vy',(x_, y_+80), font, 0.5,(255,255,255),1,cv2.LINE_AA) #Texto Vy
                #cv2.arrowedLine(frameClone, (x_, y_), (x_+ int(p2_x*0.5), int(2*y_ - p2_y)), (255, 100, 100), 1, cv2.LINE_AA,0,0.1) # vector V
                cv2.arrowedLine(frameClone, (x_, y_), (x_+ int(p2_x*0.2 - 50), int(2*y_ - p2_y)), (255, 100, 100), 1, cv2.LINE_AA,0,0.1) # vector V
                cv2.putText(frameClone,'V',(x_+ int(p2_x*0.2 - 50), int(2*y_ - p2_y)), font, 0.5,(255,255,255),1,cv2.LINE_AA) #Texto V

    "-----Dibujar trayectoria--------"#dibujar trayectoria""
    if (tiempo != 0):
        for j in range(len(lista_x)):
            cv2.circle(frameClone,(lista_x[j], lista_y[j]), 3, (0,255,255), -1)

    #Esperar el evento de una tecla para terminar
    key = cv2.waitKey(1) & 0xFF

    #Pausar simulacion
    if key == ord("p"):
        while True:
            if cv2.waitKey(1) & 0xFF == ord("p"):
                break
    #Salir de simulacion
    elif key == ord("q"):
        break

    # Presentar en una ventana la simulacion
    cv2.imshow('Simulacion lanzamiento de proyectil', frameClone)

# Actualizacion de cada frame en el video
video_capture.release()
cv2.destroyAllWindows()
