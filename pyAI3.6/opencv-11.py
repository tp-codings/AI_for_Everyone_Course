import cv2

stop = False
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")

cv2.namedWindow("myWebcam")
cv2.moveWindow('myWebcam', 0, 0)



while not stop:
    _, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayFrame, 1.05, 5)
    
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow('myWebcam', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()