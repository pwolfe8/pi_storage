import cv2
#from picamera.array import PiRGBArray
#from picamera import PiCamera
#import time

class VideoCamera(object):
    def __init__(self):
        cam = cv2.VideoCapture(0)
        cam.set(cv2.cv.CV_CAP_PROP_FPS, 30)
	cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640) 
	cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480) 	
        #self.video = cv2.VideoCapture('video.mp4')
	self.video = cam    

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()
