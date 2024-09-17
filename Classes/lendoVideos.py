import cv2

cap = cv2.VideoCapture("assets/videos/dog.mp4")

while True:
    
    _, frame = cap.read()
    cv2.imshow("Dog", frame)
    
    if cv2.waitKey(20) & 0xff==ord('d'):
        break
    
cap.release()
cv2.destroyAllWindows()
