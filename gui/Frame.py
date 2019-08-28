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
  
  def setDimensions(self, x, y):
    Container.setDimensions(self, x, y)
    self.layout.layoutWidgets(self) 
    self.recalculateRectangles()

  def setPosition(self, x, y):
    Container.setPosition(self, x, y)
    self.recalculateRectangles()

  def setPaddings(self, pad):
    Container.setPaddings(self, pad)
    self.recalculateRectangles()

  def setMargins(self, pad):
    Container.setMargins(self, pad)
    self.recalculateRectangles()

  def setBorders(self, pad):
    Container.setBorders(self, pad)
    self.recalculateRectangles()

  def recalculateRectangles(self):
    clipping_rectangle = self.getContentArea()
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
    self.layout.layoutWidgets(self)

  def addWidget(self, widget):
    Container.addWidget(self, widget)
    self.layout.layoutWidgets(self)
    self.resizeToFit()
    parent = self.getParent()
    if parent != None and isinstance(parent, Frame):
      parent.resizeToFit()

  def removeWidget(self, widget):
    Container.removeWidget(self, widget)
    self.layout.layoutWidgets(self)

  def layoutWidgets(self):
    self.layout.layoutWidgets(self)

  def resizeToFit(self):
    width = self.layout.getWidth(self)
    height = self.layout.getHeight(self)
    self.setDimensions(width, height) 

  def draw(self, surface):
    parent_clip = surface.get_clip()
   
    bg_drawer = self.getBackgroundDrawer()
    if bg_drawer != None:
      bg_drawer.drawBackground(self, surface)
    border_drawer = self.getBorderDrawer()
    if border_drawer != None:
      border_drawer.drawBorder(self, surface)
    
    # First draw the background and border:
    # Set the clipping rectangle so child widgets wont draw outside the bounds:
    clip_rect = pygame.Rect(
      self.clipping_rectangle.top_left.x, self.clipping_rectangle.top_left.y,
      self.clipping_rectangle.bottom_right.x - self.clipping_rectangle.top_left.x,
      self.clipping_rectangle.bottom_right.y - self.clipping_rectangle.top_left.y
    )
    surface.set_clip(clip_rect)
    Container.draw(self, surface)
      
    surface.set_clip(parent_clip)
    
    
