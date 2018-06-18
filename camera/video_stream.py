from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import socket
import struct

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(0.1)

# 1 sock only
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.3', 5555))

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    t = time.time()
    image = frame.array
    image = cv2.flip(image, 1)
    data = image.tobytes()
    packed_size = struct.pack("i", len(data))
    sock.sendall(packed_size)
    sock.sendall(data)
    print('\r', time.time()-t, end='')
#     cv2.imshow("i" ,image)
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break