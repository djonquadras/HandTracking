import cv2
import numpy as np

cap = cv2.VideoCapture('assets/videos/kitten.mp4')

def rescale_frame(frame: np.array,
                  scale: float = 0.75):
    largura = int(frame.shape[1]*scale)
    altura = int(frame.shape[0]*scale)
    
    return cv2.resize(frame, (largura, altura), interpolation=cv2.INTER_AREA)

def resize_frame(width: int,
                 height: int):
    
    # Somente valido para live video
    cap.set(3,width)
    cap.set(4, height)
    

# Imagem ################
"""
img = cv2.imread('assets/fotos/cat.jpg')
cv2.imshow('cat', img)

resized_img = rescale_frame(img, 2)
cv2.imshow('resized', resized_img)
cv2.waitKey(0)
"""

# Video ################
while True:
    _, frame = cap.read()
    cv2.imshow('video1', frame)
    frame = rescale_frame(frame, 0.25)
    cv2.imshow('video', frame)
    
    if cv2.waitKey(20) & 0xff== ord('d'):
        break

cap.release
cv2.destroyAllWindows