#!/usr/bin/env python
from __future__ import print_function

#import roslib
#roslib.load_manifest('beginner_tutorials')
from picamera import PiCamera
import time
import cv2
import numpy as np

import rospy
from std_msgs.msg import String

class SplitFrames(object):
    def __init__(self, pub):
        self.frame_num = 0
        self.pub = pub

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.pub.publish(buf)
            rospy.loginfo("image sent")
            self.frame_num += 1

if __name__ == '__main__':
    size = (960, 720)
    r = 30
    pub = rospy.Publisher("picamera", String, queue_size=10)
    rospy.init_node('picamera_source', anonymous=True)

    with PiCamera() as camera:
        camera.framerate = r
        camera.resolution = size
        
        output = SplitFrames(pub)
        
        camera.start_preview()
        start = time.time()
        camera.start_recording(output, format='mjpeg')
        camera.wait_recording(2)
        camera.stop_recording()
        finish = time.time()
        print('Captured %d frames at %.2ffps' % (
        output.frame_num,
        output.frame_num / (finish - start)))
