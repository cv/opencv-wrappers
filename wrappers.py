from opencv import *
from opencv.highgui import *

class Window:
    def __init__(self, name="Main Window"):
        self.name = name
        cvNamedWindow(name)
    
    def show(self, image):
        cvShowImage(self.name, image.image)
    
    def destroy(self):
        cvDestroyWindow(self.name)

class Camera:
    
    def __init__(self, id):
        self.capture = cvCreateCameraCapture(id)
        
    def frame(self):
        return Image(cvQueryFrame(self.capture))

class Image:
    
    def __init__(self, image):
        self.image = image
        self.size = cvSize(image.width, image.height)
        
    def __del__(self):
        if self and self.image:
            cvReleaseImage(self.image)
        
    def grayscale(self, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvCvtColor(self.image, result, CV_RGB2GRAY)
        return Image(result)

    def threshold(self, threshold, max_value=255, mode=CV_THRESH_BINARY, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvThreshold(self.image, result, threshold, 255, mode)
        return Image(result)
        
    def add(self, anotherImage, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvAdd(self.image, anotherImage, result)
        return Image(result)

    def sub(self, anotherImage, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvSub(self.image, anotherImage.image, result)
        return Image(result)

    def xor(self, anotherImage, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvXor(self.image, anotherImage, result)
        return Image(result)
        
    def _and(self, anotherImage, channels=1):    
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvAnd(self.image, anotherImage, result)
        return Image(result)        
    
    def _not(self, channels=1):
        result = cvCreateImage(self.size, self.image.depth, channels)
        cvNot(self.image, result)
        return Image(result)        
    
    def invert(self, channels=1):
        return self._not(channels)
        
    def nand(self, anotherImage, channels=1):
        return self._not(self.image)._and(anotherImage)

def escape_pressed():
    return cvWaitKey(10) == '\x1b'

cvStartWindowThread()    
