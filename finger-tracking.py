from wrappers import *

class FingerTracking:
  
  def __init__(self):
    self.camera = Camera(CV_CAP_ANY)
    self.window = Window()
    self.initial = False
    self.threshold = 50
    self.running = True

  def run(self):
    while self.running:
      current = self.camera.frame().grayscale()
      if not self.initial:
        self.initial = current
      self.window.show(current.sub(self.initial).threshold(self.threshold, mode=CV_THRESH_BINARY_INV))
      self._handleKeyboardEvents()


  def _handleKeyboardEvents(self):  
    key = getKeyPressed()
  
    if key == '\x1b': # escape
      self.window.destroy()
      self.running = False
  
    elif key == ' ':
      self.initial = False
    
    elif key == '+':
      self.threshold += 10
      print 'Threshold:', self.threshold
  
    elif key == '-':
      self.threshold -= 10
      print 'Threshold:', self.threshold

if __name__ == '__main__':
  FingerTracking().run()