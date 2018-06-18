import socket
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    client_socket = socket.socket()
    client_socket.connect(('192.168.1.3', 8000))

    connection = client_socket.makefile('wb')
    try:
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        # Start recording, sending the output to the connection for 60
        # seconds, then stop
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60*60)
#         camera.stop_recording()
    finally:
        connection.close()
        client_socket.close()