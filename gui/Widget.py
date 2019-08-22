from .Vector2D import *
from .Gui import *

class Pad():
  def __init__(self, left = 0, right = 0, top = 0, bottom = 0):
    self.left   = left
    self.right  = right
    self.top    = top
    self.bottom = bottom

  def __str__(self):
    return "Pad, left: %d, right: %d, top: %d, bottom: %d" % (self.left, self.right, self.top, self.bottom)
  
class Bounds():
  def __init__(self, top_left, bottom_right):
    self.top_left = top_left
    self.bottom_right = bottom_right

  def containsPoint(self, x, y = None):
    point = None
    if isinstance(x, Vector2D):
      point = x
    else: 
      point = Vector2D(x, y)

    return self.top_left < point and point < self.bottom_right

  def __str__(self):
    return "Bounds, top left: %s, bottom_right: %s" % (self.top_left, self.bottom_right)

# Base class for all the widgets. 
# A widget occupies an area that consists of content, padding around the content
# borders, and margin 
# The position of a widget is where the top left corner of the whole area of the widget is. 
class Widget():
  def __init__(self):
    self.parent = None # The parent widget of this widget
    
    self.background_drawer = None
    self.border_drawer = None

    self.position   = Vector2D() # Where the top right corner of the widget is relative to its parent
    self.dimensions = Vector2D() # The inner size of the widget
    self.paddings = Pad() # The space around the content
    self.borders  = Pad() # Border around content with padding
    self.margins  = Pad() # The margin around the content with padding and borders

  def setParent(self, parent):
    self.parent = parent


  # Calculate the absolute_position on the screen of a widget.
  def calcAbsolutePosition(self):
    parent = self.parent
    absolute_position = Vector2D(self.position)
    while parent != None :
      absolute_position += parent.getPosition()
      parent = parent.parent
      
    return absolute_position

  def setPosition(self, x, y):
    self.position.x = x
    self.position.y = y 

  def getPosition(self):
    return self.position

  def getParent(self, widget):
    return self.parent

  def setDimensions(self, x, y):
    self.dimensions.x = x
    self.dimensions.y = y

  def getDimensions(self):
    return self.dimensions

  def setPaddings(self, paddings):
    self.paddings = paddings

  def getPaddings(self):
    return self.paddings

  def setBorders(self, borders):
    self.borders = borders
  
  def getBorders(self):
    return self.borders

  def setMargins(self, margins):
    self.margins = margins

  def getMargins(self):
    return self.margins
  

  def getWidth(self):
    return self.dimensions.x

  def getPaddedWidth(self):
    return self.paddings.left + self.dimensions.x + self.paddings.right

  def getBorderedWidth(self):
    padded_width = self.getPaddedWidth()
    bordered_width = self.borders.left + padded_width + self.borders.right
    return bordered_width

  def getWholeWidth(self):
    bordered_width = self.getBorderedWidth()
    whole_width = self.margins.left + bordered_width + self.margins.right
    return whole_width

  def getHeight(self):
    return self.dimensions.y

  def getPaddedHeight(self):
    return self.paddings.top + self.dimensions.y + self.paddings.bottom

  def getBorderedHeight(self):
    padded_height = self.getPaddedHeight()
    bordered_height = self.borders.top + padded_height + self.borders.bottom
    return bordered_height

  def getWholeHeight(self):
    bordered_height = self.getBorderedHeight()
    whole_height = self.margins.top + bordered_height + self.margins.bottom
    return whole_height


  def getContentArea(self):
    absolute_position = self.calcAbsolutePosition()
    width = self.dimensions.x
    height = self.dimensions.y 

    top_left = Vector2D(
      absolute_position.x + self.margins.left + self.borders.left + self.paddings.left,
      absolute_position.y + self.margins.top + self.borders.top + self.paddings.top
    )
    
    bottom_right = top_left + Vector2D(width, height)
    return Bounds(top_left, bottom_right)
  

  def getPaddedArea(self):
    absolute_position = self.calcAbsolutePosition()
    width = self.paddings.left + self.dimensions.x + self.paddings.right
    height = self.paddings.top + self.dimensions.y + self.paddings.bottom

    top_left = Vector2D(
      absolute_position.x + self.margins.left + self.borders.left,
      absolute_position.y + self.margins.top + self.borders.top
    )
    
    bottom_right = top_left + Vector2D(width, height)
    return Bounds(top_left, bottom_right)
  


  def getBorderedArea(self):
    absolute_position = self.calcAbsolutePosition()
    width =  self.getBorderedWidth()
    height = self.getBorderedHeight()

    top_left = Vector2D(
      absolute_position.x + self.margins.left ,
      absolute_position.y + self.margins.top 
    )
    
    bottom_right = top_left + Vector2D(width, height)
    return Bounds(top_left, bottom_right)

  # Get the whole area of a widget. This includes the content dimensions, the padding
  # borders and margin. Returns new bounds
  def getWholeArea(self):
    absolute_position = self.calcAbsolutePosition()
    width =  self.getWholeWidth()
    height = self.getWholeHeight()

    top_left = absolute_position
    bottom_right = Vector2D(absolute_position.x + width, absolute_position.y + height)
    return Bounds(top_left, bottom_right)


  def setBackgroundDrawer(self, background_drawer):
    self.background_drawer = background_drawer

  def getBackgroundDrawer(self):
    return self.background_drawer

  def setBorderDrawer(self, border_drawer):
    self.border_drawer = border_drawer
 
  def getBorderDrawer(self):
    return self.border_drawer

  def onMouseOut(self, event):
    pass


  # Draw the widget
  def draw(self, surface):
    pass