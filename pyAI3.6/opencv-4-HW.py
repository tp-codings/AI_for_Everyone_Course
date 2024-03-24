import cv2
import time

stop = False

width = 640
height = 360

fpsPanel = [(0, 0),(50, 20), (0, 0, 0)]

text = "Test"

oldTime = 0

fpsFILT = 10

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while not stop:

    newTime = time.time()
    deltaTime = newTime - oldTime
    oldTime = newTime
    fps = 1/deltaTime

    fpsFILT = fpsFILT*.99+fps*.01

    _, frame = cam.read()

    text = str(int(fpsFILT))

    cv2.rectangle(frame, fpsPanel[0], fpsPanel[1], fpsPanel[2], 2)
    cv2.putText(frame, text, (5, 14), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()

