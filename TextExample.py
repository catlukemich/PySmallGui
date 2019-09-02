from Framework import *
import gui
from gui.Pad import EqualPad
from gui.Alignment import Align
from gui.Color import Color

class TextExapmple(Framework):

  def init(self, the_gui):
    font = gui.utils.loadFont("res/arial.fnt", "res/arial.png")

    # Testing labels:
    label = gui.Label(font, "Hello world")
    the_gui.addWidget(label) 
    label.setText("Hello world again")
    label.setTextColor(Color(0,0,0))


    # Text Button:
    text_button = gui.TextButton(font)
    text_button.setText("Text button")
    text_button.setPosition(100,0)
    text_button.setPaddings(EqualPad(10))
    the_gui.addWidget(text_button)

    # Text Input: 
    text_input = gui.TextInput(font)
    text_input.setPosition(300, 0)
    text_input.setPaddings(EqualPad(4))
    the_gui.addWidget(text_input) 

    # Text input in a frame:
    frame = gui.Frame()
    frame.setDimensions(100,100)
    frame.setPosition(20, 50)
    the_gui.addWidget(frame)
    text_input = gui.TextInput(font)
    
    frame.addWidget(text_input)

    # Text widget:
    text = gui.Text(400,font)
    text.setDimensions(200,200)
    text.setPosition(200,100)
    text.setText("Lorem Ipsum is simply dummy text of the printing " + \
        "and typesetting industry. Lorem Ipsum has been the industry's " +  \
        "standard dummy text ever since the 1500s, when an unknown printer " +  \
        "took a galley of type and scrambled it to make a type specimen " + \
        " book. It has survived not only five centuries, " + \
        "but also the leap into electronic typesetting, remaining essent")
    text.setTextAlign(Align.LEFT)
    text.setMaxWidth(160)
    the_gui.addWidget(text)

if __name__ == "__main__":
  example = TextExapmple()
  example.main()