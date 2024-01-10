'''
Este programa agrega a la base de datos las imagenes de la lengua de señas

Desarrolladores: 
Castillo R. Diego
Escamilla R. Aldo
Lopez S. Adair
Yañez M. Leobardo

Fecha de creacion: 14/11/2023
'''
#Importar librerias
import cv2
import os

#Importamos clases
import SeguimientoManos

#Creacion de carpeta de entrenamiento
nombre= 'D' #!Cambia la letra del abecedario
#!Cambia la direccion a tu clon del repositorio
direccion='C:/Users/yleob/OneDrive/Documentos/CarpetaDeEntrenamiento'
carpeta= direccion + '/' + nombre

#Si no esta creada la carpeta, se crea
if not os.path.exists(carpeta):
    print('Carpeta creada: ', carpeta)
    os.makedirs(carpeta)

#Captura de video y cambio de resolucion
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cont=0 # !Cambia el iterador al ultimo numero de la imagen
det = cont + 50 # Variable para detener el bucle

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
        recorte= cv2.resize(recorte, (640, 640), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("recorte", recorte)

    #Almacena imagenes para la base de datos
        cv2.imwrite("C:/Users/yleob/OneDrive/Documentos/CarpetaDeEntrenamiento/D/D_{}.jpg".format(cont), recorte) #!Cambia la ruta a una carpeta en tu escritorio
        cont= cont+1

    #Muestra la camara
    cv2.imshow("Lenguaje de senias", frame)

    esc= cv2.waitKey(1)
    #Si se presiona esc finaliza el programa
    if esc ==  27 or cont== det:
        break

cap.release()
cv2.destroyAllWindows()