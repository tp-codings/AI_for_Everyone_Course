import cv2

stop = False

width = 640
height = 360

text = "Test"

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while not stop:



    _, frame = cam.read()

    cv2.rectangle(frame, (0, 0),(390, 220), (0, 255, 0), 4)
    cv2.circle(frame, (width//2, height//2), 25, (0,0,0), 4)
    cv2.putText(frame, text, (120, 69), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

    cv2.imshow('myWebcam', frame)

    cv2.moveWindow('myWebcam', 0, 0)

    

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()