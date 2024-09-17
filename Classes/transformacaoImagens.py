import cv2
import numpy as np

# Importa Imagem
img = cv2.imread("assets/fotos/park.jpg")
type(img)
# Transladar Imagem
def translate(img, x, y):
     """Função para transladar imagens.

     Args:
         img (numpy.ndarray): Figura para transladar
         x (int): -X é esquerda, x é direita
         y (int): -y é para cima, y é para baixo
     """
     
     translation_matrix = np.float32([[1,0,x], [0,1,y]])
     
     #Dimensao das Imagens
     dimensions = (img.shape[1], img.shape[0])
     
     # Função warpAffine
     return cv2.warpAffine(img, translation_matrix, dimensions)

#cv2.imshow("Img2", translate(img, 100, -200))
# Rotacionar Imagem

def rotate(img, angle, rotation_point = None):
    
    height, width = img.shape[:2]
    
    if rotation_point is None:
        rotation_point = (width//2, height//2)
    
    # Get rotation matrix 2d
    rotaation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    
    return cv2.warpAffine(img, rotaation_matrix, dimensions)

#cv2.imshow("Rotated Img", rotate(img, 69, (69, 69)))    

# Risize Imagem
factor = 1.5 
resized = cv2.resize(img, (int(img.shape[1]*factor),int(img.shape[0]*factor)), interpolation=cv2.INTER_CUBIC)
#cv2.imshow("Img1", resized)
# Flip Imagem

flip1 = cv2.flip(img, 1) # Horizontal
flip2 = cv2.flip(img, 0) # Vertical
flip3 = cv2.flip(img, -1) # Ambos
#cv2.imshow("Img1", flip3)

# Cropp Imagem
cropped = img[100:300, 400:500]
cv2.imshow("Img1", cropped)

# Show Image
cv2.imshow("Img", img)
cv2.waitKey(0)