from .Container import *
from .Color     import *
from .BackgroundDrawer  import *
from .BorderDrawer      import *
from .GridLayout        import *
from .AbsoluteLayout    import *
from .Widget            import *

class Frame(Container):
  def __init__(self, background_color = Color(240,240,240), border_color = Color(150,150,150)):
    Container.__init__(self)

    self.layout = AbsoluteLayout()
    self.clipping_rectangle = Bounds()
  
    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())

    self.background_color = background_color
    self.border_color = border_color

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

  def recalculateClippingRectangle(self):
    clipping_rectangle = self.getPaddedArea()
    parent = self.getParent()
    while parent != None: 
      if isinstance(parent, Frame):
        parent_rect = parent.getPaddedArea()
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

  def removWidget(self, widget):
    Container.removWidget(self, widget)
    self.layout.layoutWidgets(self)

  def draw(self, surface):
    # First draw the background and border:
    bg_drawer = self.getBackgroundDrawer()
    bg_drawer.drawBackground(self, surface, self.background_color)
    
    border_drawer = self.getBorderDrawer()
    border_drawer.drawBorder(self, surface, self.border_color)
      
    
  
    # Set the clipping rectangle so child widgets wont draw outside the bounds:
    clip_rect = self.clipping_rectangle
    clipping_width  = clip_rect.bottom_right.x - clip_rect.top_left.x
    clipping_height = clip_rect.bottom_right.y - clip_rect.top_left.y
    pygame_clip_rect = pygame.Rect(
      self.clipping_rectangle.top_left.x, self.clipping_rectangle.top_left.y,
      clipping_width, clipping_height)
    
  
    surface.set_clip(pygame_clip_rect)
   # print "Pygame clip rect is: " + str(surface.get_clip())
    Container.draw(self, surface)
    surface.set_clip(None)
    
