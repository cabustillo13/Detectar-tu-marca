import cv2
import numpy as np
from matplotlib import pyplot as plt

# Ingresar elemento a analizar
numero = input("Ingrese numero de la imagen a analizar: ")
nombre = "./Imagenes/conf" + str(numero) + ".jpg"
nombrePlantilla = "./Plantilla a detectar/conf" + str(numero) + ".jpg"

# Imagen a analizar
image = cv2.imread(nombre,0)
image2 = image.copy()

# Plantilla
plantilla = cv2.imread(nombrePlantilla,0)
w, h = plantilla.shape[::-1]

# Generamos una lista con los metodos que se puede evaluar
metodos = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

cont = 0
for i in metodos:
    image = image2.copy()
    metodo = eval(i)

    # Aplicar coincidencia de plantillas
    res = cv2.matchTemplate(image,plantilla,metodo)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Si el metodo es TM_SQDIFF o TM_SQDIFF_NORMED, tome el valor minimo
    if metodo in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Colocar el rectangulo en la imagen blanco y negro -> solo tiene un canal por eso aparece 0 
    #(El rectangulo queda con una especie de color negro en la imagen)
    cv2.rectangle(image,top_left, bottom_right, 0, 4)
    cv2.imwrite('./Resultados/conf'+str(numero)+"_metodo"+str(cont)+".jpg",image)
    cont=cont+1
    
    # Graficar objeto detectado en blanco y negro para observar como funciona este metodo
    #plt.subplot(121),plt.imshow(res,cmap = 'gray')
    #plt.title('Resultado coincidente'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(image,cmap = 'gray')
    #plt.title('Punto detectado'), plt.xticks([]), plt.yticks([])
    #plt.suptitle(i)
    #plt.show()


#Bibliografia: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
