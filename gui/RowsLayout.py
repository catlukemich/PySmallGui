from .Layout import *
from .Vector2D import *
from .Alignment import *
import pprint


class RowsLayout(Layout):
  def __init__(self, align = Align.CENTER):
    self.align = align

  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
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
    offset_vector = Aligner.getAlignmentPosition(parent_size.x, parent_size.y, bounds_width, bounds_height, self.align)
    bounds_offset_left = offset_vector.x
    bounds_offset_top = offset_vector.y

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

  def getWidth(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
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
    rows_widths = []
    for widgets_array in widgets_in_rows:
      width = 0
      for widget in widgets_array:
        widget_size = widget.getWholeSize()
        width += widget_size.x
      rows_widths.append(width)
    bounds_width = max(rows_widths)
  

    return bounds_width



  def getHeight(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
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
    bounds_height = 0
       
    for height in rows_heights:
      bounds_height += height

    return bounds_height

