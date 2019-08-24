from Framework import *

class ClippingExample(Framework):

  def init(self, the_gui):
    # Testing clipping:
    frame = gui.Frame()
    frame.setPosition(20,0)
    
    frame.setMargins(Pad(4,4,4,4))
    frame.setBorders(Pad(1,1,1,1))
    frame.setDimensions(80,200)
    frame.setPaddings(EqualPad(15))
    the_gui.addWidget(frame)

    inner_frame = gui.Frame()
    inner_frame.setPosition(40,0)
    inner_frame.setMargins(Pad(4,4,4,4))
    inner_frame.setBorders(Pad(1,1,1,1))
    inner_frame.setDimensions(180,100)
    frame.addWidget(inner_frame)
    
    inner_frame.setLayout(gui.GridLayout(3,5, Align.LEFT))

    for i in range(0,12):
      col = i % 3
      row = i / 3
      
      box2 = gui.Box()
      box2.setPosition(0,0)
      #size = 10 + random.randint(0,4)
      
      width = col * 10
      height = row * 5
      
      box2.setDimensions(width, height)
      box2.setBorders(Pad(1, 1, 1, 1))
      box2.setMargins(Pad(5, 5, 5 , 5))
      inner_frame.addWidget(box2)

    img = gui.loadImage("res/aircraft.png")
    image_widget = gui.Image(img)
    image_widget.setPosition(0, 0)
    image_widget.setBorders(Pad(3,3,3,3))
    image_widget.setDimensions(100,100)
    inner_frame.addWidget(image_widget)




if __name__ == "__main__":
  example = ClippingExample()
  example.main()