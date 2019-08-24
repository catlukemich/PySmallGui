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

    #print "Drawing box"
    bg_drawer = self.getBackgroundDrawer()
    bg_drawer.drawBackground(self, surface)
    
    border_drawer = self.getBorderDrawer()
    border_drawer.drawBorder(self, surface)
