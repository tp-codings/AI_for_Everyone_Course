import cv2
import numpy as np
import requests
import time
import threading
import queue
ip_adresse_kamera1 = "http://192.168.0.2"
ip_adresse_kamera2 = "http://192.168.0.162"

oldTime = 0
fpsFILT = 20

class VideoCapture:

  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()
    
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()
        except queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()    


URL = "http://192.168.0.2"
cap = cv2.VideoCapture(URL + ":81/stream")

def hole_kamerabild(ip_adresse):
    url = f"{ip_adresse}/capture"
    response = requests.get(url)
    return np.array(cv2.imdecode(np.frombuffer(response.content, np.uint8), -1))

fenstertitel_kamera1 = "Kamera 1"
fenstertitel_kamera2 = "Kamera 2"

faceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haar\haarcascade_eye.xml")

requests.get(URL + "/control?var=framesize&val={}".format(8))


while True:

    newTime = time.time()
    deltaTime = newTime - oldTime
    oldTime = newTime
    fps = 1/deltaTime

    fpsFILT = fpsFILT*.95+fps*.05

    if cap.isOpened():
        ret, frame = cap.read()

        frames = [frame]

        for frame in frames:
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

        cv2.imshow("Output", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

# Fenstertitel festlegen


# Kamerabilder anzeigen
