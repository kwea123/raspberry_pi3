from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (960, 720)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(960, 720))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    t = time.time()
    image = frame.array
    image = cv2.flip(image, 1)
    print('\r', time.time()-t, end='')
    cv2.imshow("i" ,image)
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break