import cv2
import numpy as np

stop = False

width = 2500
height = 2500

fieldAmount = 100

fieldWidth = int(width / fieldAmount)
fieldHeight = int(height / fieldAmount)

frame = np.zeros([width , height, 3], dtype = np.uint8)

while not stop:

    for i in range(fieldAmount):
        for j in range(fieldAmount):
            frame[j*fieldWidth: (j+1)*fieldWidth, i*fieldHeight: (i+1)*fieldHeight] = ((i+j)%2) * 255



    cv2.imshow("MyWindow", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True