import cv2
import time
import numpy as np
import mediapipe as mp


# Tipagem =============================
confidence = float
webcam_image = np.ndarray
rgb_tuple = tuple[int, int, int]
#coords_vector

# Classe ==============================

class Detector:
    def __init__(self,
                 mode: bool = False,
                 number_hands: int = 2,
                 model_complexity: int = 1,
                 min_detec_confidence: confidence = 0.5,
                 min_tracking_confidence: confidence = 0.5):
        self.mode = mode
        self.number_hands = number_hands
        self.model_complexity = model_complexity
        self.detection_con = min_detec_confidence
        self.tracking_con = min_tracking_confidence
        
        # Inicializar o hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,
                                         self.number_hands,
                                         self.model_complexity,
                                         self.detection_con,
                                         self.tracking_con)
        
        self.mp_draw = mp.solutions.drawing_utils
        self.tips_ids = [4,8,12,16,20]
    
    def find_hands(self,
                   img: webcam_image,
                   draw_hands: bool = True):
        
        # Correcao de cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Coletar resultados do processo das hands e analisar
        self.results = self.hands.process(img_RGB)
        
        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
        return img
    
    def find_positions(self,
                       img: webcam_image,
                       hand_number: int = 0):
        
        self.required_lendmark_list = []
        
        my_hand = None
        if self.results.multi_hand_landmarks:
            height, width, _ = img.shape
            my_hand = self.results.multi_hand_landmarks[hand_number]
            
            for id, lm in enumerate(my_hand.landmark):
                center_x, center_y = int(lm.x*width), int(lm.y*height)
                
                self.required_lendmark_list.append([id, center_x, center_y])
                
                
        return self.required_lendmark_list


# Teste de Classe =====================
if __name__ == '__main__':
    Detec = Detector()
    
    # Captura da Imagem
    capture = cv2.VideoCapture(0)
    
 
    
    while True:
        
        
        # Captura do Frame
        _, img = capture.read()
        
        img = Detec.find_hands(img)
        landmark_list = Detec.find_positions(img)
        if landmark_list:
            print(landmark_list[8])
        
        # Mostrando o frame
        cv2.imshow('Camera', img)
        
        # Saida
        if cv2.waitKey(20) & 0xFF==ord('q'):
            break
    
    capture.release()
    cv2.destroyAllWindows()
