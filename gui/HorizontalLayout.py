from .Layout import *
from .Vector2D import *

import pprint


class HorizontalLayout(Layout):
  def __init__(self, align = Align.CENTER):
    self.align = align

  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getPaddedSize()
    
    # Calculate number of rows:
    
    widgets_in_rows = [[]]
    rows_heights = []
    rows_count = 1


    # Find out which widgets belong to which rows:
    current_end_x = 0
    current_row = 0 
    for i in range(0, len(widgets)):
      widget = widgets[i]
      next = None
      try:
        next = widgets[i + 1]
      except: pass

      widget_size = widget.getWholeSize() 
      if next != None:
        next_size = next.getWholeSize() 
      else:   
        next_size = Vector2D()

      current_end_x += widget_size.x
      widgets_in_rows[current_row].append(widget)

      if current_end_x + next_size.x > parent_size.x:
        widgets_in_rows.append([])
        current_end_x = 0
        current_row += 1
        rows_count += 1
      

    # Calculate each row height:
    for row in range(0, rows_count):
      max_height = 0
      for widget in widgets_in_rows[row]:
        height = widget.getWholeHeight()
        if height > max_height: max_height = height
      rows_heights.append(max_height)


    # Find the bounds of the layed out widgets:
    bounds_width  = 0
    bounds_height = 0
    rows_widths = []
    for widgets_array in widgets_in_rows:
      width = 0
      for widget in widgets_array:
        widget_size = widget.getWholeSize()
        width += widget_size.x
      rows_widths.append(width)
    bounds_width = max(rows_widths)
    
    for height in rows_heights:
      bounds_height += height


    # Calculate the top bounds offset and left bounds offset:
    bounds_offset_left = (parent_size.x - bounds_width) / 2
    bounds_offset_top = (parent_size.y - bounds_height) / 2
    if self.align == Align.CENTER:
      pass
    elif self.align == Align.LEFT:
      bounds_offset_left = 0
    elif self.align == Align.RIGHT:
      bounds_offset_left = parent_size.x - bounds_width
    elif self.align == Align.TOP:
      bounds_offset_top = 0
    elif self.align == Align.BOTTOM:
      bounds_offset_top = parent_size.y - bounds_height
    elif self.align == Align.TOP_LEFT:
      bounds_offset_left = 0
      bounds_offset_top = 0
    elif self.align == Align.TOP_RIGHT:
      bounds_offset_left = parent_size.x - bounds_width
      bounds_offset_top = 0
    elif self.align == Align.BOTTOM_LEFT:
      bounds_offset_left = 0
      bounds_offset_top = parent_size.y - bounds_height
    elif self.align == Align.BOTTOM_RIGHT:
      bounds_offset_left = parent_size.x - bounds_width
      bounds_offset_top = parent_size.y - bounds_height

    # Place the widgets in rows:
    current_row = 0
    for widgets_array in widgets_in_rows:
      current_y = 0
      for i in range(0, current_row):
         current_y += rows_heights[i]
      
      row_height = rows_heights[current_row]

      current_x = 0
      for widget in widgets_array:
        
        widget_size = widget.getWholeSize()
        widget_top = (row_height - widget_size.y) / 2 + current_y + bounds_offset_top
        widget.setPosition(current_x + bounds_offset_left, widget_top)
        current_x += widget_size.x
        
      current_row += 1

