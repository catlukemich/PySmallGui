from .Layout import *
from .Vector2D import *
from .Alignment import *

class ColsLayout(Layout):
  def __init__(self, align = Align.CENTER): 
    self.align = align


  def layoutWidgets(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
    # Calculate number of rows:
    
    widgets_in_cols = [[]]
    cols_widths = []
    cols_count = 1


    # Find out which widgets belong to which rows:
    current_end_y = 0
    current_col = 0 
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

      current_end_y += widget_size.y
      widgets_in_cols[current_col].append(widget)

      if current_end_y + next_size.y > parent_size.y:
        widgets_in_cols.append([])
        current_end_y = 0
        current_col += 1
        cols_count += 1
      

    # Calculate each column width:
    for col in range(0, cols_count):
      max_width = 0
      for widget in widgets_in_cols[col]:
        width = widget.getWholeWidth()
        if width > max_width: max_width = width
      cols_widths.append(max_width)


    # Find the bounds of the layed out widgets:
    bounds_width  = 0
    bounds_height = 0
    cols_heights = []
    for widgets_array in widgets_in_cols:
      height = 0
      for widget in widgets_array:
        widget_size = widget.getWholeSize()
        height += widget_size.y
      cols_heights.append(height)
    bounds_height = max(cols_heights)
    
    for width in cols_widths:
      bounds_width += width


    # Calculate the top bounds offset and left bounds offset:
    offset_vector = Aligner.getAlignmentOffset(parent_size.x, parent_size.y, bounds_width, bounds_height, self.align)
    bounds_offset_left = offset_vector.x
    bounds_offset_top = offset_vector.y

    # Place the widgets in rows:
    current_col = 0
    for widgets_array in widgets_in_cols:
      current_x = 0
      for i in range(0, current_col):
         current_x += cols_widths[i]
      
      col_width = cols_widths[current_col]

      current_y = 0
      for widget in widgets_array:
        
        widget_size = widget.getWholeSize()
        widget_left = (col_width - widget_size.x) / 2 + current_x + bounds_offset_left
        widget.setPosition(widget_left, current_y + bounds_offset_top)
        current_y += widget_size.y
        
      current_col += 1


  def getWidth(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
    # Calculate number of rows:
    
    widgets_in_cols = [[]]
    cols_widths = []
    cols_count = 1


    # Find out which widgets belong to which rows:
    current_end_y = 0
    current_col = 0 
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

      current_end_y += widget_size.y
      widgets_in_cols[current_col].append(widget)

      if current_end_y + next_size.y > parent_size.y:
        widgets_in_cols.append([])
        current_end_y = 0
        current_col += 1
        cols_count += 1
      

    # Calculate each column width:
    for col in range(0, cols_count):
      max_width = 0
      for widget in widgets_in_cols[col]:
        width = widget.getWholeWidth()
        if width > max_width: max_width = width
      cols_widths.append(max_width)


    # Find the bounds of the layed out widgets:
    bounds_width  = 0
        
    for width in cols_widths:
      bounds_width += width

    return bounds_width


  def getHeight(self, parent):
    widgets = parent.getWidgets()
    if len(widgets) == 0: return
    parent_size = parent.getContentSize()
    
    # Calculate number of rows:
    
    widgets_in_cols = [[]]
    cols_widths = []
    cols_count = 1


    # Find out which widgets belong to which rows:
    current_end_y = 0
    current_col = 0 
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

      current_end_y += widget_size.y
      widgets_in_cols[current_col].append(widget)

      if current_end_y + next_size.y > parent_size.y:
        widgets_in_cols.append([])
        current_end_y = 0
        current_col += 1
        cols_count += 1
      

    # Find the bounds of the layed out widgets:
    bounds_height = 0
    cols_heights = []
    for widgets_array in widgets_in_cols:
      height = 0
      for widget in widgets_array:
        widget_size = widget.getWholeSize()
        height += widget_size.y
      cols_heights.append(height)
    bounds_height = max(cols_heights)
    
    return bounds_height