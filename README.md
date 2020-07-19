# Detectar-tu-marca
Detectar tu marca, rótulo publicitario, banner en un evento o conferencia entre una multitud de personas o edificios.
*La idea es una especie de ¿Encontrar a Wally? en una imagen*.

Se utiliza **Template Matching** o coincidencia de plantillas: 
Es un método para buscar y encontrar la ubicación de una imagen de plantilla en una imagen más grande.

Lo que hace es simplemente deslizar la imagen de la plantilla sobre la imagen de entrada (como en convolución 2D) y compara la plantilla y el parche de la imagen de entrada debajo de la imagen de la plantilla. Hay distintos sub métodos que se pueden aplicar, se propusieron 6.

**Carpeta Imagénes:**
Contiene imágenes de convenciones, charlas, etc donde aparece una multitud de personas o muchos edificios alrededor.

**Carpeta Plantilla a detectar:**
Para cada una de las imágenes a analizar, se propone un elemento a buscar en la imagen.

**detectarObjeto.py:**
Se evalua cada plantilla en la imagen con los 6 métodos planteados. Los resultados de la coincidencia se guardan en la carpeta de *Resultados*.
Tuve un mal rendimiento respecto al método cv2.TM_CCORR y no devolvió el resultado esperado.

**multiplesObjetos.py:**
Se remarca en un rectángulo todos las plantillas detectadas en la imagen.
Ejecute el programa en una imagen icónica de Mario Bros para detectar todas las monedas que se encuentran.

Imágenes obtenidas de Pixabay.La licencia ampara: gratis para uso comercial y no requiere reconocimiento.
