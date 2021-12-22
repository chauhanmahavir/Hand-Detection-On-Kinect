from pykinect import nui
import cv2
import HandTracking as ht
import numpy as np


detector = ht.handDetector(maxHands=1)


def getColorImage(frame):
    height, width = frame.image.height, frame.image.width  #get width and height of the images
    img = np.empty((height, width, 4), np.uint8)
    frame.image.copy_bits(img.ctypes.data)                 #copy the bit of the image to the array
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)    
    img = detector.findHands(img)                       # Finding the hand
    lmlist, bbox = detector.findPosition(img)           # Getting position of hand    
    cv2.imshow('KINECT Video Stream', img) # display the image
    if cv2.waitKey(1) == 27:
        kinect.close()
        cv2.destroyAllWindows()
    

kinect = nui.Runtime()
kinect.video_frame_ready += getColorImage
kinect.video_stream.open(nui.ImageStreamType.Video, 2,nui.ImageResolution.Resolution640x480,nui.ImageType.Color)
input()


