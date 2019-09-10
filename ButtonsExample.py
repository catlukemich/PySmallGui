from Framework import *

class ButtonExample(Framework):

  def init(self, the_gui):
    font = gui.loadFont("res/arial.fnt", "res/arial.png")

    # Testing ImageButton
    label_img_button = gui.Label(font, "Image button:")
    label_img_button.setPosition(35,15)
    the_gui.addWidget(label_img_button)

    img_default = gui.loadImage("res/aircraft_bnw.png")
    img_pressed = gui.loadImage("res/aircraft.png")
    img_button = gui.ImageButton(img_default, img_pressed)
    img_button.setPosition(20, 40)
    the_gui.addWidget(img_button)
    img_button.setDimensions(100,100)

    # Testing text button:
    text_button_label = gui.Label(font, "Text button")
    text_button_label.setPosition(180, 15)
    the_gui.addWidget(text_button_label)

    text_button = gui.TextButton(font, "Click me!")
    text_button.setPosition(180, 40)
    text_button.setPaddings(gui.EqualPad(20))
    the_gui.addWidget(text_button)


    # Testing radio:
    radio_label = gui.Label(font, "Radio buttons")
    radio_label.setPosition(300, 15)
    the_gui.addWidget(radio_label)

    radio = gui.Radio(font)
    self.radio = radio
    radio.setPosition(300, 40)
    radio.addOption(0, "radiobutton 1")
    radio.addOption(1, "radiobutton 2")
    radio.addOption(2, "radiobutton 3")
    radio.addOption(3, "radiobutton 4")
    radio.addListener(RadioListener(radio))
    the_gui.addWidget(radio)


class RadioListener(gui.WidgetListener):
  def __init__(self, radio):
    self.radio = radio

  def onClick(self, widget,  event):
    print self.radio.getSelected()

if __name__ == "__main__":
  example = ButtonExample()
  example.main()