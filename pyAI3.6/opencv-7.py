import cv2

def myCallBackX(val):
    global posX
    posX = val
    print("X: ", val)
def myCallBackY(val):
    global posY
    posY = val
    print("Y: ", val)

stop = False
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 100)
cv2.moveWindow('myTrackbars', width, 0)
cv2.createTrackbar('xPos', 'myTrackbars', width//2, width, myCallBackX)
cv2.createTrackbar('yPos', 'myTrackbars', height//2, height, myCallBackY)

while not stop:
    _, frame = cam.read()

    cv2.circle(frame, (posX, posY), 25, (0,0,255), 3)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()