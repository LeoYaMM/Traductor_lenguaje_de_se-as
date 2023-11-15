'''
Este programa agrega a la base de datos las imagenes de la lengua de señas

Desarrolladores: 
Castillo R. Diego
Escamilla R. Aldo
Lopez S. Adair
Yañez M. Leobardo

Clase Desarrollada por: Santiago Sanchez Rios

Fecha de creacion: 14/11/2023
'''
#Importar librerias
import cv2
import os

#Importamos clases
import SeguimientoManos

#Creacion de carpeta de entrenamiento
nombre= 'A'
direccion='C:/Users/yleob/OneDrive/Documentos/1. Leo/ESCOM/Semestre 4/Análisis y Diseño de Sistemas/Traductor_lenguaje_de_se-as/CarpetaDeEntrnamiento'
carpeta= direccion + '/' + nombre

#Si no esta creada la carpeta, se crea
if not os.path.exists(carpeta):
    print('Carpeta creada: ', carpeta)
    os.makedirs(carpeta)

#Captura de video y cambio de resolucion
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cont=0

#Declaramos detector de mano
detector = SeguimientoManos.detectormanos(Confdeteccion=0.9)

#Bucle principal
while True:
    #Obtenemos imagen
    ret, frame = cap.read()

    #Encontramos manos
    frame = detector.encontrarmanos(frame, dibujar= True)

    #Posicion de una mano
    List1, bbox, mano = detector.encontrarposicion(frame, ManoNum=0, dibujar= True, color=[0,255,0])

    # Initialize xmin, xmax, ymin, ymax
    xmin = ymin = xmax = ymax = None

    #Si hay mano, se extraen los pixeles
    if mano== 1:
        #Es devuelto por la funcion encontrarPosicion
        xmin, ymin, xmax, ymax= bbox

    #Recortamos el frame de la mano y homogeneizamos la dimension
        recorte= frame[ymin:ymax, xmin:xmax]
        #recorte= cv2.resize(recorte, (500,500), interpolation= cv2.INTER_CUBIC)

        cv2.imshow("recorte", recorte)

    #Almacena imagenes para la base de datos
        cv2.imwrite("C:/Users/yleob/OneDrive/Escritorio/Imagenes/A_{}.jpg".format(cont), recorte)
        cont= cont+1

    #Muestra la camara
    cv2.imshow("Lenguaje de senias", frame)

    esc= cv2.waitKey(1)
    #Si se presiona esc finaliza el programa
    if esc ==  27 or cont== 100:
        break

cap.release()
cv2.destroyAllWindows()