import math
from .Layout import *
from .Vector2D import *
from .Alignment import *

class VerticalLayout(Layout):
  
  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    # Calculate the column width:
    col_width = 0
    for widget in widgets:
      width = widget.getWholeWidth()
      if width > col_width: col_width = width
    
  
    col_height = 0
    for widget in widgets:
      height = widget.getWholeHeight()
      col_height += height

    parent_size = parent.getContentSize()
    parent_offset_vector  = Aligner.getAlignmentOffset(
      parent_size.x, parent_size.y, 
      col_width, col_height, Align.CENTER)

    current_y = 0
    for widget in widgets:
      widget_size = widget.getWholeSize()  
      widget_align = widget.getAlign()
      widget_offset_vector = Aligner.getAlignmentOffset(
        col_width, 0, widget_size.x, 0, widget_align
      )
      print col_width
      print widget_offset_vector

      position_x = parent_offset_vector.x + widget_offset_vector.x
      position_y = current_y + parent_offset_vector.y+ widget_offset_vector.y
      widget.setPosition(position_x, position_y)
      
      current_y += widget_size.y
      


  def getWidth(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    # Calculate the row height:
    col_width = 0
    for widget in widgets:
      width = widget.getWholeWidth()
      if width > col_width: col_width = width
    
    return col_width

  def getHeight(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    
    col_height = 0
    for widget in widgets:
      height = widget.getWholeHeight()
      col_height += height

    return col_height




