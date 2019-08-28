from .Layout import *
from .Vector2D import *
from .Alignment import *
import pprint


class HorizontalLayout(Layout):
  
  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    # Calculate the row height:
    row_height = 0
    for widget in widgets:
      height = widget.getWholeHeight()
      if height > row_height: row_height = height
    
    row_width = 0
    for widget in widgets:
      width = widget.getWholeWidth()
      row_width += width

    parent_size = parent.getContentSize()
    parent_offset_vector  = Aligner.getAlignmentOffset(
      parent_size.x, parent_size.y, 
      row_width, row_height, Align.CENTER)

    current_x = 0
    for widget in widgets:
      widget_size = widget.getWholeSize()  
      widget_align = widget.getAlign()
      widget_offset_vector = Aligner.getAlignmentOffset(
        0, row_height, 0, widget_size.y, widget_align
      )
      position_x = current_x + parent_offset_vector.x + widget_offset_vector.x
      position_y = parent_offset_vector.y + widget_offset_vector.y
      widget.setPosition(position_x, position_y)
      
      current_x += widget_size.x

  def getWidth(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    row_width = 0
    for widget in widgets:
      width = widget.getWholeWidth()
      row_width += width

    return row_width

  def getHeight(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    # Calculate the row height:
    row_height = 0
    for widget in widgets:
      height = widget.getWholeHeight()
      if height > row_height: row_height = height
    
    return row_height

