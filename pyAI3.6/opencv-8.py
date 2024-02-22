import cv2
import numpy as np

evt = 0
pnt = (0, 0)

def mouseClick(event, posX, posY, flags, params):
    global evt 
    global pnt

    if event == cv2.EVENT_LBUTTONDOWN:
        pnt = (posX, posY)
        evt = event
        print("Positions | X: ", posX, " Y: ", posY)
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
        print(event)  

stop = False
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myWebcam')
cv2.setMouseCallback('myWebcam', mouseClick)

while not stop:
    _, frame = cam.read()

    if evt == 1:
        x = np.zeros([250, 250, 3], dtype=np.uint8)
        y = cv2.cvtColor(x, cv2.COLOR_Bgr2hs)
        clr = frame[pnt[1]][pnt[0]]
        x[:,:] = clr
        cv2.putText(x, str(clr), (0,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
        print(clr)
        cv2.imshow("Color Picker", x)
        cv2.moveWindow("Color Picker", width, 0)
        evt = 0

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()