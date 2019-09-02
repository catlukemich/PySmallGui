from Framework import *
from gui.Pad import *

class FrameExapmple(Framework):

  def init(self, the_gui):
    # Testing parenting:
    '''
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
  
   
    vertical_scrolls = gui.VerticalScrolls(None)
    vertical_scrolls.setPosition(200, 200)
    vertical_scrolls.setHeight(200)
    the_gui.addWidget(vertical_scrolls)

    horizontal_scrolls = gui.HorizontalScrolls(None)
    horizontal_scrolls.setWidth(300)
    horizontal_scrolls.setPosition(290, 200)
    the_gui.addWidget(horizontal_scrolls)
    
    '''
    


    outer_frame = gui.Frame()
    outer_frame.setDimensions(200, 200)
    outer_frame.setBorders(EqualPad(5))
    outer_frame.recalculateRectangles()
    the_gui.addWidget(outer_frame)

    scroll_frame = gui.ScrollFrame()
    scroll_frame.setPosition(100, 100)
    scroll_frame.setDimensions(100,100)
    scroll_frame.setPaddings(EqualPad(0))
    outer_frame.addWidget(scroll_frame)
   
  
    
    #print inner_frame.getClippingRectangle()
    #print outer_frame.getClippingRectangle()
    #print scroll_frame.getClippingRectangle()
    #print scroll_frame.vertical_scrolls.getClippingRectangle()
    #print scroll_frame.horizontal_scrolls.getClippingRectangle()
    

if __name__ == "__main__":
  example = FrameExapmple()
  example.main()