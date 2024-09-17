import cv2
import numpy as np


img = cv2.cvtColor(cv2.imread("assets/fotos/park.jpg"), cv2.COLOR_BGR2GRAY)

# Metodo Laplaciano
laplaciano = cv2.Laplacian(img, cv2.CV_64F)
laplaciano = np.uint8(np.absolute(laplaciano))


# Metodo de Sobel
x = cv2.Sobel(img, cv2.CV_64F, 1,0)
y = cv2.Sobel(img, cv2.CV_64F, 0,1)
sobel = cv2.bitwise_or(x,y)

# Metodo de Canny
canny = cv2.Canny(img, 150, 175)

cv2.imshow("Original", img)
cv2.imshow("Laplacian", laplaciano)
cv2.imshow("Sobel", sobel)
cv2.imshow("Canny", canny)
cv2.waitKey(0)