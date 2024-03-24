import cv2
import numpy as np

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 25
valLow = 10
valHigh = 250


def onTrack1(val):
    global hueLow
    hueLow = val
    print("Hue low ", hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("Hue High ", hueHigh)

def onTrack3(val):
    global satLow
    satLow = val
    print("Sat low ", satLow)    

def onTrack4(val):
    global satHigh
    satHigh = val
    print("Sat High ", satHigh)

def onTrack5(val):
    global valLow
    valLow = val
    print("Val low ", valLow)

def onTrack6(val):
    global valHigh
    valHigh = val
    print("Val High ", valHigh)

stop = False
width = 640
height = 360


cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("myTracker")
cv2.moveWindow("myTracker", width, 0)

cv2.createTrackbar("Hue Low1", "myTracker", 10, 179, onTrack1)
cv2.createTrackbar("Hue High1", "myTracker", 20, 179, onTrack2)
cv2.createTrackbar("Sat Low", "myTracker", 10, 255, onTrack3)
cv2.createTrackbar("Sat High", "myTracker", 250, 255, onTrack4)
cv2.createTrackbar("Val Low", "myTracker", 10, 255, onTrack5)
cv2.createTrackbar("Val High", "myTracker", 250, 255, onTrack6)

while not stop:
    _, frame = cam.read()

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myMaskSmall = cv2.resize(myMask, (width//2, height//2))
    cv2.imshow("MyMask", myMaskSmall)
    cv2.moveWindow("MyMask", 0, height)

    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall = cv2.resize(myObject, (width//2, height//2))
    cv2.imshow("MyObject", myObjectSmall)
    cv2.moveWindow("MyObject", width//2, height)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()