import cv2
import numpy as np
from matplotlib import pyplot as plt

# Imagen a analizar
imagenColor = cv2.imread('./Imagenes/conf5.jpg')
imagenGris = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2GRAY)

# Plantilla a detectar
template = cv2.imread('./Plantilla a detectar/conf5.jpg',0)
w, h = template.shape[::-1]

# Plantilla de comparacion
res = cv2.matchTemplate(imagenGris,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(imagenColor, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite("./Resultados/conf5_metodo1.jpg",imagenColor)


#Bibliografia: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
