from Layout import *

class GridLayout():
  def __init__(self, cols, rows, align = Align.CENTER):
    self.align = align
    self.cols = cols
    self.rows = rows

  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()

    widgets_widths  = []
    widgets_heights = []

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
    parent_size = parent.getContentSize()
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
