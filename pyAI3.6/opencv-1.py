import cv2

stop = False
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while not stop:
    _, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()