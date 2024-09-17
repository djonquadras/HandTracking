# Importando bibliotecas importantes
import cv2
import numpy as np
import mediapipe as mp
import math
import time

import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from handTracker import Detector

# Catpura video
caputure = cv2.VideoCapture(0)

# Configuração do CODEC de vídeo e resolução
caputure.set(cv2.CAP_PROP_FOURCC,
             cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cam_width = 1920
cam_height = 1080
caputure.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
caputure.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

# Importar o detector de mãos
hand_detector = Detector()

# Ajustar o pycaw
#https://github.com/AndreMiras/pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol = volume.GetMasterVolumeLevelScalar()
vol_old = volume.GetMasterVolumeLevelScalar()

while True:
    # Leitura de frame
    _, frame = caputure.read()
    
    # Manipulação de Frame
    img = hand_detector.find_hands(frame)
    landmarklist = hand_detector.find_positions(img)
    print(vol)
    if landmarklist:
        
        #print(landmarklist[8], landmarklist[4])
        x1, y1 = landmarklist[4][1], landmarklist[4][2]
        x2, y2 = landmarklist[8][1], landmarklist[8][2]
        
        center_x = (x1 + x2)//2
        center_y = (y1 + y2)//2
        
        
        cv2.putText(img, f"{int(vol*100)}%", (x2,y2), cv2.FONT_HERSHEY_DUPLEX,1,(30,186,35),3)
        cv2.line(img, (x1,y1), (x2,y2), (30,186,35),3)
        img = hand_detector.draw_in_position(img, [x1, x2, center_x], [y1, y2,center_y])
        lenght = math.hypot(x2-x1, y2-y1)
        
        hand_range = [20, 300]
        
        vol = (lenght-hand_range[0])/hand_range[1]
        if vol > 1: vol = 1
        if vol < 0: vol = 0
        
        volume.SetMasterVolumeLevelScalar(vol, None)
        
        
        
    
    # Exibição de frame
    cv2.imshow("Vídeo", img)
    
    # Fuga de frame
    if cv2.waitKey(20) & 0xff==ord('q'):
        break

volume.SetMasterVolumeLevelScalar(vol_old, None)
caputure.release()
cv2.destroyAllWindows()
