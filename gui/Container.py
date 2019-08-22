from .Widget import *

# Basic container class that allows grouping of widgets and laying them out.
class Container(Widget):  
 
  def __init__(self):
    Widget.__init__(self)
    self.widgets = []

  def addWidget(self, widget):
    self.widgets.append(widget)
    widget.setParent(self)

  def removeWidget(self, widget):
    self.widgets.remove(widget)
    widget.setParent(None)

  def getWidgets(self):
    return self.widgets

  def draw(self, surface):
    for widget in self.widgets:
      widget.draw(surface)