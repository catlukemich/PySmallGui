from .Widget import *
from .BackgroundDrawer  import *
from .BorderDrawer      import *
from .Color             import *
import pygame


# A simple box widget
class Box(Widget):
  def __init__(self):
    Widget.__init__(self)

    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())

    
  def draw(self, surface):
    bg_drawer = self.getBackgroundDrawer()
    if bg_drawer != None:
      bg_drawer.drawBackground(self, surface)
    
    border_drawer = self.getBorderDrawer()
    if border_drawer != None:
      border_drawer.drawBorder(self, surface)
