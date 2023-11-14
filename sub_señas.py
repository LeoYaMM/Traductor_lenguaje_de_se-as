#----Se desarrollara un sistema para traducir el lenguaje de se;as utilizando opnecv
#----Importar librerias
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

#Declaramos detector de mano
detector = SeguimientoManos.detectormanos(Confdeteccion=0.9)

#Bucle principal
while True:
    #Obtenemos imagen
    ret, frame = cap.read()
    cv2.imshow("Lenguaje de senias", frame)
    esc= cv2.waitKey(1)

    #Si se presiona esc finaliza el programa
    if esc ==  27:
        break



cap.release()
cv2.destroyAllWindows()