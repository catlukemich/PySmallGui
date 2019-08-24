from Framework import *

class FrameExapmple(Framework):

  def init(self, the_gui):
    # Testing parenting:
    frame = gui.Frame()
    frame.setPosition(100,0)
    frame.setMargins(EqualPad(4))
    frame.setBorders(EqualPad(1))
    frame.setPaddings(Pad(2,2,20,2))
    frame.setDimensions(200,200)
    #frame.setLayout(gui.GridLayout(3,4))
    frame.setLayout(gui.GridLayout(2, 4, Align.TOP))
    #frame.setLayout(gui.VerticalLayout(Align.RIGHT))
    the_gui.addWidget(frame)

    for i in range(0,8):
      
      box2 = gui.Box()
      box2.setPosition(0,0)
      #size = 10 + random.randint(0,4)
      
      width = i * 5
      height = i * 5
      
      box2.setDimensions(width, height)
      box2.setBorders(Pad(1, 1, 1, 1))
      box2.setMargins(Pad(5, 5, 5 , 5))
      frame.addWidget(box2)

    



if __name__ == "__main__":
  example = FrameExapmple()
  example.main()