from .Layout import *
from .Alignment import *

class GridLayout():
  def __init__(self, cols, rows):
    self.cols = cols
    self.rows = rows

  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()

    columns_widths  = []
    for x in range(0, self.cols): columns_widths.append([])
    rows_heights = []
    for x in range(0, self.rows): rows_heights.append([])

    columns_max_widths  = []
    rows_max_heights    = []


    # Populate the columns widths and columns heights arrays:
    i = 0
    for widget in widgets:
      size = widget.getWholeSize()
      
      widget_column = i % self.cols
      columns_widths[widget_column].append(size.x)

      widget_row = i / self.cols
      rows_heights[widget_row].append(size.y)

      i += 1


    # Calculate max columns widths and heights:
    for i in range(0, self.cols):
      max_width = 0
      widths = columns_widths[i]
      for width in widths:
        if width > max_width: max_width = width

      columns_max_widths.append(max_width)
    
    for i in range(0, self.rows):
      max_height = 0
      heights = rows_heights[i]
      for height in heights:
        if height > max_height: max_height = height

      rows_max_heights.append(max_height)


    # Calculate the bounds of all the widgets:
    bounds_width  = 0
    bounds_height = 0
    for column_max_width in columns_max_widths:   
      bounds_width += column_max_width
  
    for row_max_height in rows_max_heights:
      bounds_height += row_max_height
    
   

    # Place the widgets
    i = 0
    for widget in widgets:
      widget_size = widget.getWholeSize()
      
      widget_column = i % self.cols
      current_column_x = 0
      for col in range(0, widget_column): current_column_x += columns_max_widths[col]
    
      widget_row = i / self.cols
      current_row_y = 0
      for row in range(0, widget_row): current_row_y += rows_max_heights[row]

      max_width = columns_max_widths[widget_column]
      max_height = rows_max_heights[widget_row]

      widget_align = widget.getAlign()
      widget_offset = Aligner.getAlignmentOffset(
        max_width     , max_height, 
        widget_size.x , widget_size.y, 
        widget_align
      )
      '''
      delta_width = max_width - widget_size.x 
      offset_left = current_column_x + round(delta_width / 2.0) + widget_offset.x
      
      delta_height = max_height - widget_size.y
      offset_top =  current_row_y + round(delta_height / 2.0) + widget_offset.y
      '''

      widget.setPosition(current_column_x + widget_offset.x, current_row_y + widget_offset.y)

      i += 1


  def getWidth(self, parent):
    widgets = parent.getWidgets()

    columns_widths  = []
    for x in range(0, self.cols): columns_widths.append([])
    
    columns_max_widths  = []
    
    # Populate the columns widths and columns heights arrays:
    i = 0
    for widget in widgets:
      size = widget.getWholeSize()
      
      widget_column = i % self.cols
      columns_widths[widget_column].append(size.x)

      i += 1

    # Calculate max columns widths and heights:
    for i in range(0, self.cols):
      max_width = 0
      widths = columns_widths[i]
      for width in widths:
        if width > max_width: max_width = width

      columns_max_widths.append(max_width)
    
    total_width = 0
    for width in columns_max_widths:
      total_width += width

    return total_width


  def getHeight(self, parent):
    widgets = parent.getWidgets()

    rows_heights = []
    for x in range(0, self.rows): rows_heights.append([])

    rows_max_heights    = []

    # Populate the columns widths and columns heights arrays:
    i = 0
    for widget in widgets:
      size = widget.getWholeSize()
      
      widget_row = i / self.cols
      rows_heights[widget_row].append(size.y)

      i += 1


    # Calculate max rows heights:
    for i in range(0, self.rows):
      max_height = 0
      heights = rows_heights[i]
      for height in heights:
        if height > max_height: max_height = height

      rows_max_heights.append(max_height)

    total_height = 0
    for height in rows_max_heights:
      total_height += height

    return total_height
