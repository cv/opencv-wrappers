from wrappers import *

camera = Camera(CV_CAP_ANY)
window = Window()
initial = False

while True:

  current = camera.frame().grayscale().invert()

  if not initial:
    initial = current

  window.show(current.sub(initial).threshold(20, mode=CV_THRESH_BINARY_INV))

  if escape_pressed():
    window.destroy()
    break
