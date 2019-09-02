import random
from Framework import *
from gui.Alignment import Align

class LayoutExapmple(Framework):

  def init(self, the_gui):
    # Testing absolute layout:

    frame = gui.Frame()
    frame.setPosition(50,50)
    frame.setPaddings(EqualPad(10))
    frame.setDimensions(200,200)
    the_gui.addWidget(frame)

      
    inner_frame1 = gui.Frame()
    inner_frame1.setPosition(0,0)
    inner_frame1.setDimensions(50,50)
    frame.addWidget(inner_frame1)
    
    inner_frame2 = gui.Frame()
    inner_frame2.setPosition(0, 60)
    #inner_frame2.setPaddings(EqualPad(5))
    inner_frame2.setDimensions(50,50)
    frame.addWidget(inner_frame2)
      
    inner_inner_frame = gui.Frame()
    inner_inner_frame.setPosition(20,20)
    inner_inner_frame.setDimensions(50, 50)
    inner_frame2.addWidget(inner_inner_frame)
    
    img = gui.loadImage("res/aircraft.png")
    img_widget = gui.Image(img)
    #img_widget.setDimensions(50,50)
    the_gui.addWidget(img_widget)




    # Testing horizontal layout:
    frame = gui.Frame()
    frame.setPosition(200,0)
    frame.setLayout(gui.HorizontalLayout())
    the_gui.addWidget(frame)

    for i in range(0,8):
      box = gui.Box()
      width = i * 5
      height = random.randint(10, 20)
      box.setDimensions(width, height)
      box.setAlign(Align.TOP)
      frame.addWidget(box)

    


    # Testing vertical layout:
    frame = gui.Frame()
    frame.setPosition(400,0)
    frame.setLayout(gui.VerticalLayout())
    the_gui.addWidget(frame)

    for i in range(0,8):
      box = gui.Box()
      width = i * 5
      height = random.randint(10, 20)
      box.setDimensions(width, height)
      box.setAlign(Align.TOP)
      frame.addWidget(box)

    

    # Testing rows layout:
    
    frame = gui.Frame()
    frame.setPosition(600,0)
    frame.setDimensions(100, 40)
    frame.setLayout(gui.RowsLayout())
    the_gui.addWidget(frame)

    for i in range(0,8):
      box = gui.Box()
      width = i * 5
      height = random.randint(10, 20)
      box.setDimensions(width, height)
      box.setAlign(Align.TOP)
      frame.addWidget(box)

    


    # Testing cols layout:
    frame = gui.Frame()
    frame.setPosition(800,0)
    frame.setDimensions(40, 100)
    frame.setLayout(gui.ColsLayout())
    the_gui.addWidget(frame)

    for i in range(0,8):
      box = gui.Box()
      width = i * 5
      height = random.randint(10, 20)
      box.setDimensions(width, height)
      box.setAlign(Align.TOP)
      frame.addWidget(box)

    

    # Testing grid layout:
    frame = gui.Frame()
    frame.setPosition(0,200)
    frame.setPaddings(gui.EqualPad(1))
    frame.setDimensions(40, 100)
    frame.setLayout(gui.GridLayout(2,6))
    the_gui.addWidget(frame)

    for i in range(0,12):
      box = gui.Box()
      width = i * 5
      height = random.randint(0, 20)
      box.setDimensions(width, height)
      box.setAlign(Align.CENTER)
      frame.addWidget(box)

    
    # Testing nested layouts:
    outer_frame = gui.Frame()
    outer_frame.setPosition(200, 200)
    outer_frame.setPaddings(Pad(10,10,10,10))
    outer_frame.setLayout(gui.VerticalLayout())

    the_gui.addWidget(outer_frame)

    inner_frame1 = gui.Frame()
    inner_frame1.setAlign(Align.CENTER)
    inner_frame1.setLayout(gui.HorizontalLayout())
    outer_frame.addWidget(inner_frame1)
    
    images = ["aircraft.png", "truck.png", "forklift.png"]
    for image in images:
      path = "res/" + image
      img = gui.loadImage(path)
      img_widget = gui.Image(img)
      img_widget.setDimensions(20,20)
      inner_frame1.addWidget(img_widget)


    font = gui.loadFont("res/arial.fnt", "res/arial.png")
    inner_frame2 = gui.Frame()
    inner_frame2.setLayout(gui.GridLayout(2,4))
    inner_frame2.setDimensions(100,100)
    outer_frame.addWidget(inner_frame2)
    images = ["gamepad.png", "bulldozer.png", "plant.png", "folder.png"]
    for image in images:
      path = "res/icons/" + image
      label = gui.Label(font)
      label.setText(image)
      label.setAlign(Align.RIGHT)
      inner_frame2.addWidget(label)
      img = gui.loadImage(path)
      img_widget = gui.Image(img)
      img_widget.setDimensions(40,40)
      inner_frame2.addWidget(img_widget)

    text_input = gui.TextInput(font, 50)
    outer_frame.addWidget(text_input)

if __name__ == "__main__":
  example = LayoutExapmple()
  example.main()