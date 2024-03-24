import cv2
import numpy as np

hueLow1 = 10
hueHigh1 = 20
hueLow2 = 170
hueHigh2 = 179
satLow = 10
satHigh = 25
valLow = 10
valHigh = 250


def onTrack1(val):
    global hueLow1
    hueLow1 = val
    print("Hue low ", hueLow1)
def onTrack2(val):
    global hueHigh1
    hueHigh1 = val
    print("Hue High ", hueHigh1)

def onTrack7(val):
    global hueLow2
    hueLow2 = val
    print("Hue low ", hueLow2)
def onTrack8(val):
    global hueHigh2
    hueHigh2 = val
    print("Hue High ", hueHigh2)

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
cv2.createTrackbar("Hue Low2", "myTracker", 10, 179, onTrack7)
cv2.createTrackbar("Hue High2", "myTracker", 20, 179, onTrack8)
cv2.createTrackbar("Sat Low", "myTracker", 10, 255, onTrack3)
cv2.createTrackbar("Sat High", "myTracker", 250, 255, onTrack4)
cv2.createTrackbar("Val Low", "myTracker", 10, 255, onTrack5)
cv2.createTrackbar("Val High", "myTracker", 250, 255, onTrack6)

while not stop:
    _, frame = cam.read()

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound1 = np.array([hueLow1, satLow, valLow])
    upperBound1 = np.array([hueHigh1, satHigh, valHigh])

    lowerBound2 = np.array([hueLow2, satLow, valLow])
    upperBound2 = np.array([hueHigh2, satHigh, valHigh])

    myMask1 = cv2.inRange(frameHSV, lowerBound1, upperBound1)
    myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)

    myMaskSmall1 = cv2.resize(myMask1, (width//2, height//2))
    cv2.imshow("MyMask1", myMaskSmall1)
    cv2.moveWindow("MyMask1", width//2, height)

    myMaskSmall2 = cv2.resize(myMask2, (width//2, height//2))
    cv2.imshow("MyMask2", myMaskSmall2)
    cv2.moveWindow("MyMask2", width, height)

    myMask = cv2.bitwise_or(myMask1, myMask2)

    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall = cv2.resize(myObject, (width//2, height//2))
    cv2.imshow("MyObject", myObjectSmall)
    cv2.moveWindow("MyObject", 0, height)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()