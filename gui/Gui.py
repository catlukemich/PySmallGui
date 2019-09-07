from .Widget import *
from .Container import *
from .Input import *
from .Vector2D import *
from .Frame import *
from .Pad import *

class Gui(Container, MouseListener, KeyboardListener):
  def __init__(self, input):
    Container.__init__(self)
    self.hover_widget = None
    self.focus_widget = None
    self.active_widget = None
    self.drag_widget = None

    self.setMargins(EqualPad(0))
    self.setBorders(EqualPad(0))
    self.setPaddings(EqualPad(0))

  def mouseButtonDown(self, event):
    if self.hover_widget != None:
      event_consumed = self.hover_widget.onMouseButtonDown(event)
      self.drag_widget = self.hover_widget
      if event_consumed: return True

    old_focus = self.focus_widget
    new_focus = self.hover_widget
    if old_focus != None:
      old_focus.onFocusLost(event)
    if new_focus != None:
      new_focus.onFocusGain(event)

    self.focus_widget = self.hover_widget
    self.active_widget = self.hover_widget
    print "New focus widget: " + str(self.focus_widget)

    return False

  def mouseMotion(self, event):
    event_consumed = False
    if self.drag_widget != None:
      event_consumed = self.drag_widget.onDrag(event)
      if event_consumed: return True # The event is consumed by dragging a widget.

    old_hover_widget = self.hover_widget
    new_hover_widget = self.findHoverWidget(event.pos[0], event.pos[1])
    if new_hover_widget != old_hover_widget:

      if old_hover_widget != None:
        event_consumed = old_hover_widget.onMouseOut(event)

      if new_hover_widget != None:
        event_consumed = new_hover_widget.onMouseOver(event)

      self.hover_widget = new_hover_widget
      if event_consumed: return True

    if old_hover_widget == new_hover_widget and old_hover_widget != None and new_hover_widget != None:
      event_consumed = self.hover_widget.onMouseMove(event)
      if event_consumed: return True

    return False
 
  def findHoverWidget(self, mouse_x, mouse_y, parent = None):
    if parent == None:
      widgets = self.getWidgets()
    else:
      widgets = parent.getWidgets()

    widgets = reversed(widgets)

    for widget in widgets:
      if isinstance(widget, Container):
        parent = widget
        hover_widget = self.findHoverWidget(mouse_x, mouse_y, parent)
        if hover_widget == None:
          parent_area = parent.getBorderedArea()
          if isinstance(widget, Frame):
            parent_area = widget.getHoverRectangle()
          mouse = Vector2D(mouse_x, mouse_y)
          if parent_area.containsPoint(mouse):
            return parent
          
        else: return hover_widget
      else:
        widget_area = widget.getBorderedArea()
        mouse = Vector2D(mouse_x, mouse_y)
        parent = widget.getParent()
  
        if parent != None and isinstance(parent, Frame):
          parent_hover_rectangle = parent.getHoverRectangle()
          widget_area = widget_area.intersection(parent_hover_rectangle)
        if widget_area.containsPoint(mouse):
          return widget
        

    return None


    
  def mouseButtonUp(self, event):
    event_consumed = False

    self.drag_widget = None

    if self.hover_widget != None:
      event_consumed = self.hover_widget.onMouseButtonUp(event)
    if self.hover_widget != None and self.active_widget != None and self.hover_widget == self.active_widget:
      event_consumed = self.active_widget.onClick(event)

    return event_consumed




  def keyDown(self, event):
    event_consumed = False
    if self.focus_widget != None:
      event_consumed = self.focus_widget.onKeyDown(event)
    return event_consumed
