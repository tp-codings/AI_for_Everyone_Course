import cv2

cam = cv2.VideoCapture(0)

stop = False

width, height = 640, 480

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

screens = [(0, 0, "col1", 1), (1, 0, "gray1", 0), (0, 1, "gray2", 0), (1, 1, "col2", 1)]

while not stop:

    _, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for screen in screens:
        if(screen[3] == 1):
            cv2.imshow(screen[2], frame)
        else:
            cv2.imshow(screen[2], grayFrame)
        cv2.moveWindow(screen[2], screen[0] * width, screen[1] * height)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True


