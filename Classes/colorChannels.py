import cv2
import numpy as np

# Lê as imagens
img = cv2.imread("assets/fotos/park.jpg")

# Cria um canva em branco
canva = np.zeros(img.shape[:2], dtype="uint8")

# Separa nas cores
blue, green, red = cv2.split(img)

# Reintegra as cores

blue = cv2.merge([red, green, blue])
green = cv2.merge([canva, green, canva])
red = cv2.merge([canva, canva, red])

#cv2.imshow("Green", green)
cv2.imshow("Blue", blue)
#cv2.imshow("Red", red)
cv2.imshow("Park", img)
cv2.waitKey(0)