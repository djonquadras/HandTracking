import cv2
import numpy as np

# Criar Canva
canva = np.zeros([400,400], dtype='uint8')

rectangle = cv2.rectangle(canva.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(canva.copy(), (200,200), 200, 255, -1)

# Bitwise AND 
bitwise_and = cv2.bitwise_and(rectangle, circle)

# Bitwiase OR
bitwise_or = cv2.bitwise_or(rectangle, circle)

# Bitwiase XOR
bitwise_xor = cv2.bitwise_xor(rectangle, circle)

# Bitwiase NOT
bitwise_not = cv2.bitwise_not(rectangle)

cv2.imshow("And", bitwise_not)

#cv2.imshow("Canva", canva)
cv2.imshow("Rect", rectangle)
cv2.imshow("Circ", circle)
cv2.waitKey(0)