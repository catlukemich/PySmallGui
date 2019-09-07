from .Vector2D import *
from .Gui import *
from .Bounds import *
from .Pad import Pad
from .Pad import EqualPad
from .Alignment import Align

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
    self.dimensions = Vector2D(20,20) # The inner size of the widget
    self.paddings = Pad(0) # The space around the content
    self.borders  = EqualPad(1) # Border around content with padding
    self.margins  = Pad() # The margin around the content with padding and borders
    
    self.align = Align.CENTER

    self.listeners = []
    
  def setParent(self, parent):
    self.parent = parent

  def getParent(self):
    return self.parent

  # Calculate the absolute_position on the screen of a widget.
  def calcAbsolutePosition(self):
    absolute_position = Vector2D(self.position) 
    parent = self.parent

    while parent != None :
      absolute_position += parent.getPosition()
      
      borders = parent.getBorders()
      absolute_position.x += borders.left
      absolute_position.y += borders.top

      margins = parent.getMargins()
      absolute_position.x += margins.left
      absolute_position.y += margins.top

      paddings = parent.getPaddings()
      absolute_position.x += paddings.left
      absolute_position.y += paddings.top
      
      parent = parent.getParent()

    
    return absolute_position

  def getPosition(self):
    return self.position

  
  def setPosition(self, x, y = None):
    if isinstance(x, Vector2D):
      self.position = x
    else:
      self.position.x = x
      self.position.y = y 

  def setDimensions(self, x, y = None):
    if isinstance(x, Vector2D):
      self.dimensions = x
    else:
      self.dimensions.x = x
      self.dimensions.y = y
    from .Frame import Frame
    if self.parent != None and isinstance(self.parent, Frame):
      self.parent.layoutWidgets()
      self.parent.resizeToFit()
 
  def getDimensions(self):
    return self.dimensions

  def setPaddings(self, paddings):
    self.paddings = paddings
    from .Frame import Frame
    if self.parent != None and isinstance(self.parent, Frame):
      self.parent.layoutWidgets()

  def getPaddings(self):
    return self.paddings

  def setBorders(self, borders):
    self.borders = borders
    from .Frame import Frame
    if self.parent != None and isinstance(self.parent, Frame):
      self.parent.layoutWidgets()
  
  def getBorders(self):
    return self.borders

  def setMargins(self, margins):
    self.margins = margins
    from .Frame import Frame
    if self.parent != None and isinstance(self.parent, Frame):
      self.parent.layoutWidgets()

  def getMargins(self):
    return self.margins
  
  def setWidth(self, width):
    dims = Vector2D(self.getDimensions())
    dims.x = width
    self.setDimensions(dims)

  def getWidth(self):
    return self.dimensions.x

  def setHeight(self, height):
    dims = Vector2D(self.getDimensions())
    dims.y = height
    self.setDimensions(dims)
    
  def getHeight(self):
    return self.dimensions.y

  def setAlign(self, align):
    self.align = align

  def getAlign(self):
    return self.align

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

  def getContentSize(self):
    return self.dimensions

  def getPaddedSize(self):
    width = self.paddings.left + self.dimensions.x + self.paddings.right
    height = self.paddings.top + self.dimensions.y + self.paddings.bottom
    return Vector2D(width, height)

  def getBorderedSize(self):
    padded_size = self.getPaddedSize()
    width = self.borders.left + padded_size.x + self.borders.right
    height = self.borders.top + padded_size.y + self.borders.bottom
    return Vector2D(width, height)

  def getWholeSize(self):
    bordered_size = self.getBorderedSize()
    width = self.margins.left + bordered_size.x + self.margins.right
    height = self.margins.top + bordered_size.y + self.margins.bottom
    return Vector2D(width, height)
  

  def setBackgroundDrawer(self, background_drawer):
    self.background_drawer = background_drawer

  def getBackgroundDrawer(self):
    return self.background_drawer

  def setBorderDrawer(self, border_drawer):
    self.border_drawer = border_drawer
 
  def getBorderDrawer(self):
    return self.border_drawer

  def setBackgroundColor(self, color):
    if self.background_drawer != None:
      self.background_drawer.setColor(color)

  def setBorderColor(self, color):
    if self.border_drawer != None:
      self.border_drawer.setColor(color)

  def onMouseOver(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onMouseOver(self, event)
      if consumed: break
    return consumed

  def onMouseMove(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onMouseMove(self, event)
      if consumed: break
    return consumed

  def onMouseOut(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onMouseOut(self, event)
      if consumed: break
    return consumed

  def onKeyDown(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onKeyDown(self, event)
      if consumed: break
    return consumed

  def onMouseButtonDown(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onMouseButtonDown(self, event)
      if consumed: break
    return consumed

  def onMouseButtonUp(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onMouseButtonUp(self, event)
      if consumed: break
    return consumed

  def onDrag(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onDrag(self, event)
      if consumed: break
    return consumed

  def onClick(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onClick(self, event)
      if consumed: break
    return consumed

  def onFocusGain(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onFocusGain(self, event)
      if consumed: break
    return consumed

  def onFocusLost(self, event):
    consumed = False
    for listener in self.listeners:
      consumed = listener.onFocusLost(self, event)
      if consumed: break
    return consumed

  # Draw the widget
  def draw(self, surface):
    pass

  def addListener(self, listener):
    self.listeners.append(listener)

  def removeListener(self, listener):
    self.listeners.remove(listener)