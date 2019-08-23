class GridLayout():
  def __init__(self, cols, rows):
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

    i = 0
    for widget in widgets:
      size = widget.getWholeSize()
      
      widget_column = i % self.cols
      columns_widths[widget_column].append(size.x)

      widget_row = i / self.cols
      rows_heights[widget_row].append(size.y)

      i += 1

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
      offset_left = current_column_x + delta_width / 2
      
      delta_height = max_height - widget_size.y
      offset_top = current_row_y + delta_height / 2

      widget.setPosition(offset_left, offset_top)

      i += 1
