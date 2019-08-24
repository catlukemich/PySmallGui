from Framework import *

class ButtonExample(Framework):

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


    # Testing ImageButton
    img_default = gui.loadImage("res/aircraft_bnw.png")
    img_pressed = gui.loadImage("res/aircraft.png")
    img_button = gui.ImageButton(img_default, img_pressed)
    img_button.setPosition(90, 20)
    img_button.setDimensions(100,100)
    the_gui.addWidget(img_button)





if __name__ == "__main__":
  example = ButtonExample()
  example.main()