from Framework import *
from gui.Pad import *

class FrameExapmple(Framework):

  def init(self, the_gui):
    # Testing parenting:
 
    frame = gui.Frame()
    frame.setPosition(0,0)
    frame.setMargins(EqualPad(0))
    frame.setBorders(EqualPad(1))
    frame.setPaddings(Pad(0,0,0,0))
    frame.setDimensions(200,200)
    #frame.setLayout(gui.GridLayout(3,4))
    frame.setLayout(gui.GridLayout(2, 4))
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

      
    font = gui.loadFont("res/arial.fnt", "res/arial.png")

    label_frame = gui.LabelFrame(font)
    label_frame.setPosition(150,0)
    label_frame.setLabelText("A label frame")
    the_gui.addWidget(label_frame)

    label_frame.setLayout(gui.GridLayout(4,4))
    label_frame.setLabelPaddings(EqualPad(10))
    label_frame.setPaddings(EqualPad(10))  

    for y in range(0,4):
      for x in range(0,4):
        text = "Col: %d, row: %d" % (x, y)
        label = gui.Label(font, text)
        label_frame.addWidget(label)
  
   
  
    scroll_frame = gui.ScrollFrame(gui.Scrolls.HORIZONTAL_AND_VERTICAL)
    scroll_frame.setPosition(10, 200)
    scroll_frame.setDimensions(100,100)
    scroll_frame.setPaddings(EqualPad(0))
    scroll_frame.setLayout(gui.GridLayout(4,10))
    the_gui.addWidget(scroll_frame)
   
    for y in range(0,10):
      for x in range(0,4):
        label = gui.Label(font)
        txt = "Col: %d, Row: %d" % (x, y)
        label.setText(txt)
        scroll_frame.addWidget(label)
  
    


if __name__ == "__main__":
  example = FrameExapmple()
  example.main()