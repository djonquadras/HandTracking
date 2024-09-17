import cv2
import numpy as np

# Cores -> BRG e nao RGB
azul = 255,0,0
verde = 0,255,0
vermelho = 0,0,255
aleatorio = 69,69,69
aleatorio2 = 100,100,100

# Ler as imagens
blank_img = np.zeros((500, 500, 3), dtype='uint8')
cat = cv2.imread('assets/fotos/cat.jpg')

# Pintando blank por operacao matricial

# Pintar toda a matriz
blank_img[:] = azul
blank_img[:] = vermelho
blank_img[:] = verde

# Desenhando

# Retangulo
cv2.rectangle(blank_img,(10,10), (110,20), vermelho, 3)

cv2.rectangle(blank_img, (30,30), (blank_img.shape[1]//4, blank_img.shape[0]//4), azul, 2)

# Circulo

(2*(69**2))**(1/2)


cv2.circle(blank_img, (250,250), 69, aleatorio, 3)

# Linha

cv2.line(blank_img, (250+49,250+49), (250,250), aleatorio2, 3)
cv2.line(blank_img, (250,250), (250-49,250+49), aleatorio2, 3)
cv2.line(blank_img, (250,250+69), (250,250-69), aleatorio2, 3)

# Texto

cv2.putText(blank_img, "Oi Mozao", (69,69), cv2.FONT_HERSHEY_COMPLEX, 1.5, (203,255,192), 3)
cv2.imshow('blank', blank_img)
cv2.waitKey(0)