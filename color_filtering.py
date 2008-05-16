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
  
    if key == '\x1b': # escape
      self.window.destroy()
      self.running = False

    elif key == 'g':
      self.colour = createGreenImage(cvSize(640, 480))

    elif key == 'b':
      self.colour = createBlueImage(cvSize(640, 480))

    elif key == 'r':
      self.colour = createRedImage(cvSize(640, 480))

if __name__ == '__main__':
  ColorFiltering().run()