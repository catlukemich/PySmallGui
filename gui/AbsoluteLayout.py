from .Layout import *
import sys

class AbsoluteLayout(Layout):
  def getWidth(self, parent):
    widgets = parent.getWidgets()
    min_x = sys.maxint
    max_x = 0
    
    for widget in widgets:
      area = widget.getWholeArea()
      if area.top_left.x < min_x: min_x = area.top_left.x
      if area.bottom_right.x > max_x: max_x = area.bottom_right.x

    return max_x - min_x

  def getWidth(self, parent):
    widgets = parent.getWidgets()
    min_y = sys.maxint
    max_y = 0
    
    for widget in widgets:
      area = widget.getWholeArea()
      if area.top_left.y < min_y: min_y = area.top_left.y
      if area.bottom_right.y > max_y: max_y = area.bottom_right.y

    return max_y - min_y