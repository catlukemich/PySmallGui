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
  
    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())


  def setParent(self, parent):
    Widget.setParent(self, parent)
    self.recalculateClippingRectangle()
  
  def setDimensions(self, x, y):
    Widget.setDimensions(self, x, y)
    self.layout.layoutWidgets(self) 
    self.recalculateClippingRectangle()

  def setPosition(self, x, y):
    Widget.setPosition(self, x, y)
    self.recalculateClippingRectangle()

  def setPaddings(self, pad):
    Widget.setPaddings(self, pad)
    self.recalculateClippingRectangle()

  def setMargins(self, pad):
    Widget.setMargins(self, pad)
    self.recalculateClippingRectangle()

  def setBorders(self, pad):
    Widget.setBorders(self, pad)
    self.recalculateClippingRectangle()

  def recalculateClippingRectangle(self):
    clipping_rectangle = self.getBorderedArea()
    parent = self.getParent()
    while parent != None: 
      if isinstance(parent, Frame):
        parent_rect = parent.getBorderedArea()
        clipping_rectangle = parent_rect.intersection(clipping_rectangle)
      
      parent = parent.getParent()

    self.clipping_rectangle = clipping_rectangle

  def getClippingRectangle(self):
    return self.clipping_rectangle

  def setLayout(self, layout):  
    self.layout = layout
    self.layout.layoutWidgets(self)

  def addWidget(self, widget):
    Container.addWidget(self, widget)
    self.layout.layoutWidgets(self)

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
    # First draw the background and border:
    bg_drawer = self.getBackgroundDrawer()
    bg_drawer.drawBackground(self, surface)
    
    # Set the clipping rectangle so child widgets wont draw outside the bounds:
    clip_rect = self.clipping_rectangle
    clipping_width  = clip_rect.bottom_right.x - clip_rect.top_left.x
    clipping_height = clip_rect.bottom_right.y - clip_rect.top_left.y
    pygame_clip_rect = pygame.Rect(
      self.clipping_rectangle.top_left.x, self.clipping_rectangle.top_left.y,
      clipping_width, clipping_height)
    
    surface.set_clip(pygame_clip_rect)
    Container.draw(self, surface)
    border_drawer = self.getBorderDrawer()
    border_drawer.drawBorder(self, surface)
      
    surface.set_clip(None)
    
    
