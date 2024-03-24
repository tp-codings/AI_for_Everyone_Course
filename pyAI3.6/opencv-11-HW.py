import cv2
import time
stop = False
width = 640
height = 360

oldTime = 0
fpsFILT = 20

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haar\haarcascade_eye.xml")

cv2.namedWindow("myWebcam")
cv2.moveWindow('myWebcam', 0, 0)



while not stop:

    newTime = time.time()
    deltaTime = newTime - oldTime
    oldTime = newTime
    fps = 1/deltaTime

    fpsFILT = fpsFILT*.95+fps*.05

    _, frame = cam.read()

    cv2.putText(frame, str(int(fpsFILT)), (5, 14), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayFrame, 1.05, 5)
    
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        faceROI = frame[y:y+h, x:x+w]
        faceROIGray = cv2.cvtColor(faceROI, cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(faceROIGray, 1.05, 5)

        for eye in eyes:
            xe,ye,we,he = eye
            cv2.rectangle(frame[y:y+h, x:x+w], (xe,ye), (xe+we, ye+he), (0, 0, 255), 1)


        

    cv2.imshow('myWebcam', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

cam.release()