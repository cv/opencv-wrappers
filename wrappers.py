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
    cvSetCaptureProperty(self.capture, CV_CAP_PROP_FRAME_WIDTH, 640);
    cvSetCaptureProperty(self.capture, CV_CAP_PROP_FRAME_HEIGHT, 480);
      
  def frame(self):
    return Image(cvQueryFrame(self.capture))

class Image:

  def __init__(self, image):
    self.image = image
    self.size = cvSize(image.width, image.height)
      
  def __del__(self):
    if self and self.image:
      cvReleaseImage(self.image)
  
  def fill(self,r,g,b):
    cvSet(self.image, cvScalar(r, g, b))
    return self
      
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
    
  #Francisco: Trying some color filtering  
  def filterColorUsingRGB(self, channels=1):  
    #compute which pixels are in the wanted range
    # ranges for the limitation of the histogram
    
    rgb_min = CV_RGB(100, 255, 100);
    rgb_max = CV_RGB(0, 0, 0)
    result = cvCreateImage(self.size, self.image.depth, channels)
    cvInRangeS (self.image, rgb_min, rgb_max, result)
    
    return Image(result)
      
  #Francisco: Trying some color filtering  
  def filterColorUsingHSV(self, channels=1):  
    # compute the hsv version of the image 
    hsvImage = cvCreateImage(self.size, self.image.depth, 3)
    cvCvtColor (self.image, hsvImage, cv.CV_BGR2HSV)
    
    return Image(hsvImage)
    
    # compute which pixels are in the wanted range
    # ranges for the limitation of the histogram
    vmin = 10
    vmax = 256
    smin = 30
    hsv_min = cvScalar (0, smin, vmin, 0)
    hsv_max = cvScalar (180, 256, vmax, 0)
    result = cvCreateImage(self.size, self.image.depth, channels)
    cvInRangeS (hsvImage, hsv_min, hsv_max, result)
    
    return Image(result)
    
def getKeyPressed(wait=10):
  return cvWaitKey(wait)
  
def createImage(size, depth=IPL_DEPTH_8U, channels=1):
  return Image(cvCreateImage(size, depth, channels))

def createBlueImage(size):
  return createImage(size, channels=3).fill(255,0,0)

def createGreenImage(size):
  return createImage(size, channels=3).fill(0,255,0)

def createRedImage(size):
  return createImage(size, channels=3).fill(0,0,255)

def createYellowImage(size):
  return createImage(size, channels=3).fill(0,255,255)

def createFuchsiaImage(size):
  return createImage(size, channels=3).fill(255,0,255)

def createCyanImage(size):
  return createImage(size, channels=3).fill(255,255,0)

cvStartWindowThread()    
