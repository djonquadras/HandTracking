import cv2

# Function Image Read
img = cv2.imread('assets/fotos/cat.jpg')

# Show the picture
cv2.imshow('Name', img)
cv2.waitKey(0)
