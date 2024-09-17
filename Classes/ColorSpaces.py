import cv2
import numpy as np

# RGB é o padrão em várias ferramentas
# BGR é o padrão no cv2

# Ler Imagem
img = cv2.imread("assets/fotos/cat.jpg")

# Para escala de cinza
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gato", img)


cv2.waitKey(0)