from .Layout import *
from .Alignment import *

class GridLayout():
  def __init__(self, cols, rows, align = Align.CENTER):
    self.align = align
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
        if height > max_height: max_width = height

      rows_max_heights.append(max_width)


    # Calculate the bounds of all the widgets:
    bounds_width  = 0
    bounds_height = 0
    for column_max_width in columns_max_widths:   
      bounds_width += column_max_width
  
    for row_max_height in rows_max_heights:
      bounds_height += row_max_height
    
    # Calculate the top bounds offset and left bounds offset:
    bounds_parent = parent.getDimensions()
    offset_vector = Aligner.getAlignmentPosition(
      bounds_parent.x, bounds_parent.y, 
      bounds_width, bounds_height,
      self.align
    )
  
    bounds_offset_left = offset_vector.x
    bounds_offset_top = offset_vector.y
    

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

      delta_width = max_width - widget_size.x
      offset_left = bounds_offset_left + current_column_x + delta_width / 2
      
      delta_height = max_height - widget_size.y
      offset_top = bounds_offset_top + current_row_y + delta_height / 2 

      widget.setPosition(offset_left, offset_top)

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
        if height > max_height: max_width = height

      rows_max_heights.append(max_width)

    total_height = 0
    for height in rows_max_heights:
      total_height += height

    return total_height
