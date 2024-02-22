import cv2

posX = 0
posY = 0

def changePosX(val):
    global posX
    posX = val
    print("X: ", val)
def changePosY(val):
    global posY
    posY = val
    print("Y: ", val)

def changeSize(val):
    width = val
    height = int(val*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, height)

stop = False
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 200)
cv2.moveWindow('myTrackbars', width, 0)
cv2.createTrackbar('xPos', 'myTrackbars', 0, 1920, changePosX)
cv2.createTrackbar('yPos', 'myTrackbars', 0, 1080, changePosY)
cv2.createTrackbar('xSize', 'myTrackbars', width, 1920, changeSize)

while not stop:
    _, frame = cam.read() 

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', posX, posY)


    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()