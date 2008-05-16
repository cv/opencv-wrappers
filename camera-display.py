from wrappers import *

camera = Camera(CV_CAP_ANY)
window = Window()

while True:
  window.show(camera.frame())
  if getKeyPressed() == '\x1b': # escape
    window.destroy()
    break
