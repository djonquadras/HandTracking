import cv2
import numpy as np

#Le a imagem
img = cv2.imread("assets/fotos/cats.jpg")

#Cria o Canva
canva = np.zeros(img.shape[:2], dtype='uint8')

#Circle
circle = cv2.circle(canva.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# Retangulo
rectangle = cv2.rectangle(canva.copy(), (30,30), (370,370), 255, -1)

# Criando máscaras diferentes
recorte1 = cv2.bitwise_and(circle, rectangle)
recorte2 = cv2.bitwise_or(circle, rectangle)
recorte3 = cv2.bitwise_not(circle)

# Mascaras
mask1 = cv2.bitwise_and(img, img, mask = recorte1)
mask2 = cv2.bitwise_and(img, img, mask = recorte2)
mask3 = cv2.bitwise_and(img, img, mask = recorte3)


cv2.imshow("Gatos", img)
cv2.imshow("Mask 1", mask1)
cv2.imshow("Mask 2", mask2)
cv2.imshow("Mask 3", mask3)
#cv2.imshow("Rect", rectangle)
cv2.waitKey(0)