import cv2
import numpy as np

# Lendo os 3 canais de cores
img = cv2.imread('assets/fotos/cat.jpg')
img2 = cv2.imread('assets/fotos/park.jpg')

# Converter para Preto e Branco
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cinza2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Blur (borrar)

blurred = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=cv2.BORDER_DEFAULT)
blurred2 = cv2.GaussianBlur(img2, ksize=(3,3), sigmaX=cv2.BORDER_DEFAULT)

# Deteccao de Borda - Edge Cascade

edge1 = cv2.Canny(blurred, threshold1=250, threshold2=200)
edge2 = cv2.Canny(blurred2, threshold1=250, threshold2=200)


# Dilatacao de Imagens

dilatada = cv2.dilate(edge1, (9,9), iterations=3)
dilatada2 = cv2.dilate(edge2, (9,9), iterations=3)

# Corroer Imagem - Eroding Image

corroer1 = cv2.erode(dilatada, (9,9), iterations=3)
corroer2 = cv2.erode(dilatada2, (9,9), iterations=3)


# Resize
resized1 = cv2.resize(img, (300,300))
resized2 = cv2.resize(img2, (300,300))

# Crop

corte1 = img[50:200, 200:400]
corte2 = img2[50:200, 200:400]

cv2.imshow('gato', corte1)
cv2.imshow('parque', corte2)



cv2.waitKey(0)