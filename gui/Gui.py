from .Container import *
from .Input import *
from .Vector2D import *

class Gui(Container, MouseListener, KeyboardListener):
  def __init__(self, input):
    Container.__init__(self)
    self.hover_widget = None
    self.focus_widget = None
    
  def mouseMotion(self, event):
    self.hover_widget = self.findHoverWidget(event.pos[0], event.pos[1])

  def findHoverWidget(self, mouse_x, mouse_y, parent = None)
    if parent == None:
      widgets = self.getWidgets()
    else:
      widgets = parent.getWidgets()
    
    for widget in widgets:
      if isinstance(widget, Container):
        parent = widget
        hover_widget = self.findHoverWidget(parent)
        if hover_widget == None:
          return parent
        else return hover_widget
      else:
        absolute_position = widget.calcAbsolutePosition()
        top_left = absolute_position
        widget_area = widget.getArea()
        bottom_right = absolute_position + widget_area
        mouse = Vector2D(mouse_x, mouse_y)
  
        if top_left < mouse and mouse > bottom_right:
          return widget