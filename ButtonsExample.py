from Framework import *

class ButtonExample(Framework):

  def init(self, the_gui):
   
    # Testing parenting:
    frame = gui.Frame()
    frame.setPosition(100,100)
    #frame.setMargins(EqualPad(4))
    #frame.setLayout(gui.GridLayout(1, 1))
    frame.setLayout(gui.VerticalLayout())
    frame.setDimensions(80,80)    
    frame.setBorders(Pad(1,1,1,1))
    frame.setPaddings(Pad(0,0,0,30))
    the_gui.addWidget(frame)
    
    # Testing ImageButton
    img_default = gui.loadImage("res/aircraft_bnw.png")
    img_pressed = gui.loadImage("res/aircraft.png")
    img_button = gui.ImageButton(img_default, img_pressed)
   
    frame.addWidget(img_button)
    img_button.setDimensions(100,100)





if __name__ == "__main__":
  example = ButtonExample()
  example.main()