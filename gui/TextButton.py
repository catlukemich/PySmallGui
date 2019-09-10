from .BackgroundDrawer import *
from .BorderDrawer     import *
from .PressedBackgroundDrawer import PressedBackgroundDrawer
from .PressedBorderDrawer     import PressedBorderDrawer
from .Label import Label

class TextButton(Label):
  def __init__(self, font, text = ""):
    Label.__init__(self, font, text)

    self.released_background_drawer = BackgroundDrawer()
    self.released_border_drawer = BorderDrawer()
    self.setBackgroundDrawer(self.released_background_drawer)
    self.setBorderDrawer(self.released_border_drawer)

    self.pressed_background_drawer = PressedBackgroundDrawer()
    self.pressed_border_drawer = PressedBorderDrawer()


  def onMouseButtonDown(self, event):
    Label.onMouseButtonDown(self, event)
    self.setBackgroundDrawer(self.pressed_background_drawer)
    self.setBorderDrawer(self.pressed_border_drawer)
    

  def onMouseButtonUp(self, event):
    Label.onMouseButtonUp(self, event)
    self.setBackgroundDrawer(self.released_background_drawer)
    self.setBorderDrawer(self.released_border_drawer)

  def onMouseOut(self, event):
    self.setBackgroundDrawer(self.released_background_drawer)
    self.setBorderDrawer(self.released_border_drawer)

  def setPressedBackgroundDrawer(self, bg_drawer):  
    self.pressed_background_drawer = bg_drawer

  def setPressedBorderDrawer(self, border_drawer):
    self.pressed_border_drawer = border_drawer