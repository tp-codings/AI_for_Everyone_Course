import cv2
evt = 0
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ', event)
        print('at Position', xPos, yPos)
        pnt = (xPos, yPos)
        evt = event

    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event Was: ', event)
        print('at Position', xPos, yPos)
        evt = event
        pnt = (xPos, yPos)

    if event==cv2.EVENT_RBUTTONUP:
        print('Mouse Event Was: ', event)
        print('at Position', xPos, yPos)
        evt = event
        pnt = (xPos, yPos)

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

ROIpos1 = (0, 0)
ROIpos2 = (1, 1)
show = False

while not stop:
    _, frame = cam.read()

    if evt == 1:
        ROIpos1 = pnt
    if evt == 4: 
        ROIpos2 = pnt
        if ROIpos2 != ROIpos1:
            cv2.rectangle(frame, ROIpos1, ROIpos2, (0,0,255), 2)
            myROI = frame[ROIpos1[1]:ROIpos2[1], ROIpos1[0]:ROIpos2[0]]   
            cv2.imshow('myROI', myROI)
            cv2.moveWindow('myROI', width, 0)
            frame[ROIpos1[1]:ROIpos2[1], ROIpos1[0]:ROIpos2[0]] = myROI
    if evt == 5:
        cv2.destroyWindow('myROI')
        evt = 0
    print(ROIpos1, " ", ROIpos2)

        

    cv2.imshow('myWebcam', frame) 
    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()