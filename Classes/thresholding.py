import cv2
import numpy as np

img = cv2.imread("assets/fotos/cats.jpg")
cv2.imshow("cats", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# daptative Threshold
#adaptThreshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,9)
adaptThreshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_Ce, cv2.THRESH_BINARY_INV, 11,9)

cv2.imshow('Exemplo', adaptThreshold)
cv2.waitKey(0)