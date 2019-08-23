from .Widget import *
from .BackgroundDrawer  import *
from .BorderDrawer      import *
from .Color             import *
import pygame


# A simple box widget
class Box(Widget):
  def __init__(self, background_color = Color(240,240,240), border_color = Color(150,150,150)):
    Widget.__init__(self)

    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())

    self.background_color = background_color
    self.border_color = border_color
  
    
  def draw(self, surface):

    #print "Drawing box"
    bg_drawer = self.getBackgroundDrawer()
    bg_drawer.drawBackground(self, surface, self.background_color)
    
    border_drawer = self.getBorderDrawer()
    border_drawer.drawBorder(self, surface, self.border_color)
    

  def __str__(self):
    return "Box"
