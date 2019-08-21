from .Vector2D import *

class Pad():
  def __init__(self):
    self.left   = 0
    self.right  = 0
    self.top    = 0
    self.bottom = 0

# Base class for all the widgets. 
# A widget occupies an area that consists of content, padding around the content
# borders, and margin 
# The position of a widget is where the top left corner of the whole area of the widget is. 
class Widget():
  def __init__(self):
    self.parent = None # The parent widget of this widget
    
    self.position   = Vector2D() # Where the top right corner of the widget is relative to its parent
    self.dimensions = Vector2D() # The inner size of the widget
    self.padding = Pad() # The space around the content
    self.border  = Pad() # Border around content with padding
    self.margin  = Pad() # The margin around the content with padding and borders

  def setParent(self, widget):
    self.parent = parent

  def setPosition(self, x, y):
    self.position.x = x
    self.position.y = y 

  # Calculate the absolute_position on the screen of a widget.
  def calcAbsolutePosition(self):
    parent = self.parent
    absolute_position = Vector2D(self.position)
    while parent != None:
      absolute_position += parent.getPosition()
      parent = parent.parent
      
    return absolute_position

  def getPosition(self):
    return self.position

  def getParent(self, widget):
    return self.parent

  def setDimensions(self, x, y):
    self.dimensions.x = x
    self.dimensions.y = y

  def getDimensiond(self):
    return self.dimensions

  def setPadding(self, padding):
    self.padding = padding

  def getPadding(self):
    return self.padding

  def setMargin(self, margin):
    self.margin = margin

  def getMargin(self)
    return self.margin
  
  # Get the whole area of a widget. This includes the content dimensions, the padding
  # borders and margin.
  def getArea(self):
    width =  \
      self.dimensions.x + \ 
      self.padding.left + self.padding.right + \
      self.border.left + self.border.right + \
      self.margin.left + self.margin.right

    height = \
      self.dimensions.y + \
      self.padding.top + self.padding.bottom + \
      self.border.top + self.border.bottom + \
      self.margin.top + self.margin.bottom 

    return Vector2D(width, height)

  # Draw the widget
  def draw(self, surface):
    pass