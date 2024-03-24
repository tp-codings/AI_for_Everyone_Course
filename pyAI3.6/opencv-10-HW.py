import cv2
import numpy as np

hueLow1 = 18
hueHigh1 = 24
hueLow2 = 9
hueHigh2 = 0
satLow = 135
satHigh = 217
valLow = 203
valHigh = 245


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
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("myTracker")
cv2.moveWindow("myTracker", width, 0)

cv2.createTrackbar("Hue Low1", "myTracker", hueLow1, 179, onTrack1)
cv2.createTrackbar("Hue High1", "myTracker", hueHigh1, 179, onTrack2)
cv2.createTrackbar("Hue Low2", "myTracker", hueLow2, 179, onTrack7)
cv2.createTrackbar("Hue High2", "myTracker", hueHigh2, 179, onTrack8)
cv2.createTrackbar("Sat Low", "myTracker", satLow, 255, onTrack3)
cv2.createTrackbar("Sat High", "myTracker", satHigh, 255, onTrack4)
cv2.createTrackbar("Val Low", "myTracker", valLow, 255, onTrack5)
cv2.createTrackbar("Val High", "myTracker", valHigh, 255, onTrack6)

cv2.namedWindow("myWebcam")
cv2.moveWindow('myWebcam', 0, 0)


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

    contours, junk = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (255, 0, 0), 3)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 300:
            #cv2.drawContours(frame, [contour], 0, (255, 0, 0), 3)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0, 255), 3)
            xPos = x / width * 1920
            yPos = y / height * 1080
            cv2.moveWindow("myWebcam", int(xPos), int(yPos))


    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall = cv2.resize(myObject, (width//2, height//2))
    cv2.imshow("MyObject", myObjectSmall)
    cv2.moveWindow("MyObject", 0, height)

    cv2.imshow('myWebcam', frame)



    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()