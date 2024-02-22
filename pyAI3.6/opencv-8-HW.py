import cv2
import numpy as np

stop = False
width = 640
height = int(width * 9 / 16)

cam = cv2.VideoCapture(0)

while not stop:
    x = np.zeros([height, width, 3], dtype=np.uint8)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2HSV)

    y = np.zeros([height, width, 3], dtype=np.uint8)
    y = cv2.cvtColor(y, cv2.COLOR_BGR2HSV)

    for i in range(height):
        for j in range(width):
            x[i][j] = (j * 180 / width, 255, i)
            y[i][j] = (j * 180 / width, i, 255)

    x = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)
    y = cv2.cvtColor(y, cv2.COLOR_HSV2BGR)

    cv2.imshow("HSV1", x)
    cv2.moveWindow("HSV1", 0, 0)
    cv2.imshow("HSV2", y)
    cv2.moveWindow("HSV2", 0, height + 30)

    if cv2.waitKey(1) & 0xff == ord('q'):
        stop = True

