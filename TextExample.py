from Framework import *
import gui

class TextExapmple(Framework):

  def init(self, the_gui):
    # Testing labels:
    font = gui.utils.loadFont("res/arial.fnt", "res/arial.png")
    label = gui.Label(font, "Hello world")
    the_gui.addWidget(label) 



if __name__ == "__main__":
  example = TextExapmple()
  example.main()