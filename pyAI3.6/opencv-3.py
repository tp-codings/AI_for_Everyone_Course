import cv2
import numpy as np

stop = False

frame = np.zeros([250, 250, 3], dtype = np.uint8)

while not stop:


    frame[:125, :125] = [0, 0, 255]
    frame[:122, :] = [255, 0, 0]

    cv2.imshow("MyWindow", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True