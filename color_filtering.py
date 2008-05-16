from wrappers import *

class ColorFiltering:
  def __init__(self):

    self.camera = Camera(CV_CAP_ANY)
    self.window = Window()
    self.running = True
    self.colour = False
    
  #Francisco: Trying some color filtering  
  def filterColorUsingHSV(self, channels=1):  
    # compute the hsv version of the image 
    hsvImage = cvCreateImage(self.size, self.depth, channels)
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
    
  #Francisco: Trying some color filtering  
  def filterColorUsingRGB(self, image, channels=1):  
    #compute which pixels are in the wanted range
    # ranges for the limitation of the histogram
    
    bmin=50#0;
    bmax=70#110;#190
    gmin=60#0;
    gmax=90#85;#62
    rmin=140#45;#134
    rmax=256#256;#254
    
    
    # Make an image file for colors.
    bimg = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    gimg = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    rimg = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
 
    # Split image into individual channels
    cvSplit(image.image,bimg,gimg,rimg,None);
 
    # Create intensity color map
    intensity = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    cvAdd(bimg,gimg,intensity);
    cvAdd(intensity,rimg, intensity);
    
    #Calculate rgb ratios
    cvDiv(bimg, intensity, bimg, 256);
    cvDiv(gimg, intensity, gimg, 256);
    cvDiv(rimg, intensity, rimg, 256);
 
    # Create rcup mask
    car = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    bcar = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    gcar = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    rcar = cvCreateImage(image.size, IPL_DEPTH_8U, 1)
    cvInRangeS(bimg, cvRealScalar(bmin), cvRealScalar(bmax), bcar);
    cvInRangeS(gimg, cvRealScalar(gmin), cvRealScalar(gmax), gcar);
    cvInRangeS(rimg, cvRealScalar(rmin), cvRealScalar(rmax), rcar);
    
    
    cvAnd(bcar, gcar, car);
    cvAnd(car, rcar, car);
 
    # Filter out noise
    cvErode(car, car, None, 2);
    cvDilate(car, car, None, 2);
    
    return Image(car)
    
  def run(self):
    while self.running:
      current = self.camera.frame()
#      self.window.show(self.filterColorUsingRGB(current))
      
      if not self.colour:
        self.colour = createGreenImage(current.size)

      output = current.sub(self.colour, channels=3)

      self.window.show(output)
      self._handleKeyboardEvents()

  def _handleKeyboardEvents(self):  
    key = getKeyPressed()

    size = cvSize(640,480)

    r = createRedImage(size)
    g = createGreenImage(size)
    b = createBlueImage(size)
    y = createYellowImage(size)
    f = createFuchsiaImage(size)
    c = createCyanImage(size)
    
    if key == '\x1b': # escape
      self.window.destroy()
      self.running = False

    elif key == '1':
      self.colour = r

    elif key == '2':
      self.colour = g

    elif key == '3':
      self.colour = b

    elif key == '4':
      self.colour = y

    elif key == '5':
      self.colour = f

    elif key == '6':
      self.colour = c

if __name__ == '__main__':
  ColorFiltering().run()