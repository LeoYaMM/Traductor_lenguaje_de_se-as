#Importar librerias
import cv2
import os
from ultralytics import YOLO

#Importamos clases
import SeguimientoManos

#Captura de video y cambio de resolucion
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

model = YOLO('best.pt')

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
        resultados = model.predict(recorte, conf = 0.45)

        if len(resultados) != 0:
            for results in resultados:
                masks = results.masks
                coordenadas = masks

                anotaciones = resultados[0].plot()

        cv2.imshow("recorte", anotaciones)

    #Muestra la camara
    cv2.imshow("Lenguaje de senias", frame)

    esc= cv2.waitKey(1)
    #Si se presiona esc finaliza el programa
    if esc ==  27:
        break

cap.release()
cv2.destroyAllWindows()