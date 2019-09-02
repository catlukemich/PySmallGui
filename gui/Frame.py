from .Container import *
from .Color     import *
from .BackgroundDrawer  import *
from .BorderDrawer      import *
from .GridLayout        import *
from .AbsoluteLayout    import *
from .Widget            import *

class Frame(Container):
  def __init__(self):
    Container.__init__(self)

    self.layout = AbsoluteLayout()
    self.clipping_rectangle = Bounds()
    self.hover_rectangle = Bounds()

    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())
    

  def setParent(self, parent):
    Container.setParent(self, parent)
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()
  
  def setDimensions(self, x, y = None):
    Container.setDimensions(self, x, y)
    self.layoutWidgets()
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()

  def setPosition(self, x, y):
    Container.setPosition(self, x, y)
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()

  def setPaddings(self, pad):
    Container.setPaddings(self, pad)
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()

  def setMargins(self, pad):
    Container.setMargins(self, pad)
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()

  def setBorders(self, pad):
    Container.setBorders(self, pad)
    self.recalculateRectangles()
    for widget in self.widgets:  
      if isinstance(widget, Frame):
        widget.recalculateRectangles()

  def recalculateRectangles(self):
    #print "-------recalculateRectangles-----"
    #print "Self is : \t" + str(self)
    clipping_rectangle = self.getContentArea()
    #print "cnt area:\t" + str(clipping_rectangle)

    hover_rectangle = self.getBorderedArea()
    parent = self.getParent()
    while parent != None: 
      if isinstance(parent, Frame):
        parent_clipping_rectangle = parent.getContentArea()
        clipping_rectangle = parent_clipping_rectangle.intersection(clipping_rectangle)
        hover_rectangle = hover_rectangle.intersection(parent_clipping_rectangle)
      
      parent = parent.getParent()

    self.clipping_rectangle = clipping_rectangle
    self.hover_rectangle = hover_rectangle

  def getClippingRectangle(self):
    return self.clipping_rectangle

  def getHoverRectangle(self):
    return self.hover_rectangle

  def setLayout(self, layout):  
    self.layout = layout
    self.layoutWidgets()

  def addWidget(self, widget):
    Container.addWidget(self, widget)
    self.layout.layoutWidgets(self)
    self.resizeToFit()
    parent = self.getParent()
    if parent != None and isinstance(parent, Frame):
      parent.resizeToFit()

  def removeWidget(self, widget):
    Container.removeWidget(self, widget)
    self.layoutWidgets()
    if isinstance(widget, Frame):
      widget.recalculateRectangles()

  def layoutWidgets(self):
    self.layout.layoutWidgets(self)

  def resizeToFit(self):
    width = self.layout.getWidth(self)
    height = self.layout.getHeight(self)
    self.setDimensions(width, height) 

  def draw(self, surface):
    abs_pos  = self.calcAbsolutePosition()
    
    parent_clip = surface.get_clip()
   
    bg_drawer = self.getBackgroundDrawer()
    if bg_drawer != None:
      bg_drawer.drawBackground(self, surface)
    border_drawer = self.getBorderDrawer()
    if border_drawer != None:
      border_drawer.drawBorder(self, surface)
    
    # First draw the background and border:
    # Set the clipping rectangle so child widgets wont draw outside the bounds:

    clipping_rectangle = self.clipping_rectangle
    clip_rect = pygame.Rect((
      clipping_rectangle.top_left.x, clipping_rectangle.top_left.y,
      clipping_rectangle.bottom_right.x - clipping_rectangle.top_left.x,
      clipping_rectangle.bottom_right.y - clipping_rectangle.top_left.y
    ))
    #print clip_rect

    surface.set_clip(clip_rect)
    if self.clipping_rectangle.top_left.x == self.clipping_rectangle.bottom_right.x or  self.clipping_rectangle.top_left.y == self.clipping_rectangle.bottom_right.y:
      print self.clipping_rectangle
    else:
      Container.draw(self, surface)
      
    surface.set_clip(parent_clip)
    
    
