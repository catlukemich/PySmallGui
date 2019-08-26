import random
from Framework import *
from gui.Alignment import Align

class LayoutExapmple(Framework):

  def init(self, the_gui):
    # Testing horizontal layout:
    frame = gui.Frame()
    frame.setPosition(0,0)
    frame.setDimensions(200,200)
    frame.setLayout(gui.HorizontalLayout())
    the_gui.addWidget(frame)

    for i in range(0,8):
      
      box = gui.Box()
      box.setPosition(0,0)
      #size = 10 + random.randint(0,4)
      
      width = i * 5
      height = random.randint(10, 20)
      
      box.setDimensions(width, height)
      box.setBorders(Pad(1, 1, 1, 1))
      box.setMargins(Pad(5, 5, 5 , 5))
      box.setAlign(Align.TOP)

      frame.addWidget(box)

    frame.resizeToFit()



if __name__ == "__main__":
  example = LayoutExapmple()
  example.main()