from wrappers import *

class ColorFiltering:
  def __init__(self):

    self.camera = Camera(CV_CAP_ANY)
    self.window = Window()
    self.running = True
    self.colour = False

  def run(self):
    while self.running:
      current = self.camera.frame()
      
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