from wrappers import *

class ColorFiltering:
  def __init__(self):

    self.camera = Camera(CV_CAP_ANY)
    self.window = Window()
    self.running = True

  def run(self):
    while self.running:
      current = self.camera.frame()
      
      green = createImage(current.size, current.image.depth)
      green.setColor(0,255,255,0)
            
      self.window.show(green)
      self._handleKeyboardEvents()

  def _handleKeyboardEvents(self):  
    key = getKeyPressed()
  
    if key == '\x1b': # escape
      self.window.destroy()
      self.running = False
if __name__ == '__main__':
  ColorFiltering().run()