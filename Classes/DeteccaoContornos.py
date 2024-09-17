import cv2
import numpy as np

#Lendo a imagem
img = cv2.imread("assets/fotos/cats.jpg")
cv2.imshow("Gatos", img)

# Canva Branco de mesmo tamanho
blank_canva = np.zeros(img.shape, dtype="uint8")

# Escala de cinza
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

########### Detecção de Contornos ###########

# Borrar Imagem
img = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)

# Canny
img = cv2.Canny(img, 125, 175)

# Find Conturs
"""
Opções de Métodos  de Aproximação de Contorno:
- cv2.CHAIN_APPROX_NONE: usa uma linha inteira
- cv2.CHAIN_APPROX_SIMPLE: Apenas os extremos
"""
contorno, hierarquia = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("Gatos 2", img)

cv2.drawContours(blank_canva, contorno, -1, (0,0,255))

cv2.imshow("Contornos", blank_canva)

cv2.waitKey(0)