from .Container import *
from .Input import *
from .Vector2D import *

class Gui(Container, MouseListener, KeyboardListener):
  def __init__(self, input):
    Container.__init__(self)
    self.hover_widget = None
    self.focus_widget = None
    
  def mouseMotion(self, event):
    old_hover_widget = self.hover_widget
    new_hover_widget = self.findHoverWidget(event.pos[0], event.pos[1])
    if new_hover_widget != old_hover_widget:
      if old_hover_widget != None:
        old_hover_widget.onMouseOut(event)
      if new_hover_widget != None:
        new_hover_widget.onMouseOver(event)
      print "Hover widget is: " + str(self.hover_widget)
      

  def findHoverWidget(self, mouse_x, mouse_y, parent = None):
    if parent == None:
      widgets = self.getWidgets()
    else:
      widgets = parent.getWidgets()
    
    for widget in widgets:
      if isinstance(widget, Container):
        parent = widget
        hover_widget = self.findHoverWidget(mouse_x, mouse_y, parent)
        if hover_widget == None:
          parent_area = parent.getBorderedArea()
          mouse = Vector2D(mouse_x, mouse_y)
          if parent_area.containsPoint(mouse):
            return parent
          
        else: return hover_widget
      else:
        widget_area = widget.getBorderedArea()
        mouse = Vector2D(mouse_x, mouse_y)
  
        if widget_area.containsPoint(mouse):
          return widget

    return None

  def mouseButtonDown(self, event):
    if self.hover_widget != None:
      self.focus_widget = self.hover_widget

