import pygame
from .Frame import Frame
from .Box import Box
from .Pad import Pad
from .Pad import EqualPad
from .Vector2D import Vector2D
from .utils import *
from .Color import Color

class Scrolls():
  VERTICAL = 1
  HORIZONTAL = 2
  HORIZONTAL_AND_VERTICAL = 3


class ScrollUpArrow(Box):
  def __init__(self, vertical_scrolls):
    Box.__init__(self)
    self.vertical_scrolls = vertical_scrolls
    self.setDimensions(11,11)
    self.setBorders(Pad(0,0,0,1))

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    # Draw a triangle arrow:
    top_co = (area.top_left.x + 5, area.top_left.y + 2)
    bottom_left_co = (area.top_left.x + 1, area.top_left.y + 8)
    bottom_right_co = (area.top_left.x + 9, area.top_left.y + 8)
    pygame.draw.polygon(surface, pygame.Color(0,0,0,255), [top_co, bottom_left_co, bottom_right_co])

  def onClick(self, event):
    old_percentage = self.vertical_scrolls.getScrollPercentage()
    new_percentage = old_percentage - 10
    self.vertical_scrolls.scrollToPercentage(new_percentage)

class ScrollDownArrow(Box):
  def __init__(self, vertical_scrolls):
    Box.__init__(self)
    self.vertical_scrolls = vertical_scrolls
    self.setDimensions(11,11)
    self.setBorders(Pad(0,0,1,0))

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    # Draw a triangle arrow:
    top_left_co = (area.top_left.x + 1, area.top_left.y + 2)
    top_right_co = (area.top_left.x + 9, area.top_left.y + 2)
    bottom_co = (area.top_left.x + 5, area.top_left.y + 8)
    pygame.draw.polygon(surface, pygame.Color(0,0,0,255), [top_left_co, top_right_co, bottom_co])

  def onClick(self, event):
    old_percentage = self.vertical_scrolls.getScrollPercentage()
    new_percentage = old_percentage + 10
    self.vertical_scrolls.scrollToPercentage(new_percentage)

class VerticalKnob(Box):
  def __init__(self, vertical_scrolls):
    Box.__init__(self)
    self.vertical_scrolls = vertical_scrolls
  
    self.setWidth(11)
    self.setHeight(30)
    
    self.setBorders(Pad(0,0,1,1))
    
    self.is_scrolling = False

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    height = self.getHeight()
    width = self.getWidth()

    middle = round(height / 2.0)
    
    line1_co1 = (area.top_left.x + 2, area.top_left.y + middle - 2)
    line1_co2 = (area.top_left.x + width - 2, area.top_left.y +  middle -2)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line1_co1, line1_co2)

    line2_co1 = (area.top_left.x + 2, area.top_left.y + middle)
    line2_co2 = (area.top_left.x + width - 2, area.top_left.y + middle)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line2_co1, line2_co2)

    line3_co1 = (area.top_left.x + 2, area.top_left.y +  middle + 2)
    line3_co2 = (area.top_left.x + width - 2 , area.top_left.y + middle + 2)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line3_co1, line3_co2)
    

  def onMouseButtonDown(self, event):
    if event.button == 1:
      self.is_scrolling = True

  def onMouseButtonUp(self, event):
    if event.button == 1:
      self.is_scrolling = False

  def onMouseOut(self, event):
    self.is_scrolling = False

  def onMouseMove(self, event):
    if self.is_scrolling:
      scrolls_height = self.vertical_scrolls.getHeight()
      own_height = self.getWholeHeight()
      up_arrow_height   = self.vertical_scrolls.scroll_up_arrow.getWholeHeight()
      down_arrow_height = self.vertical_scrolls.scroll_down_arrow.getWholeHeight()
      
      mouse_rel_y = event.rel[1]
      own_pos = Vector2D(self.getPosition())
      own_pos.y += mouse_rel_y

      if own_pos.y < up_arrow_height: 
        own_pos.y = up_arrow_height
      if own_pos.y > scrolls_height - own_height - down_arrow_height: 
        own_pos.y = scrolls_height - own_height - down_arrow_height
  
      self.setPosition(own_pos)

      scroll_percentage = mapRange(
        own_pos.y, 
        up_arrow_height,  scrolls_height - down_arrow_height - own_height ,
        0, 100
      ) 
      self.vertical_scrolls.setScrollPercentage(scroll_percentage)
      


class VerticalScrolls(Frame):
  def __init__(self, scroll_frame):
    Frame.__init__(self)
    self.scroll_frame = scroll_frame
    self.scroll_percentage = 0

    self.setBorders(Pad(1,0,0,0))

    self.scroll_up_arrow = ScrollUpArrow(self)
    self.scroll_down_arrow = ScrollDownArrow(self)
    self.knob = VerticalKnob(self)
  
    Frame.addWidget(self, self.scroll_down_arrow)
    Frame.addWidget(self, self.scroll_up_arrow)
    Frame.addWidget(self, self.knob)
 
    self.setWidth(11)
     
  def layoutWidgets(self):
    Frame.layoutWidgets(self)
    up_arrow_height = self.scroll_up_arrow.getWholeHeight()
    self.knob.setPosition(0, up_arrow_height)
    own_dimensions = self.getDimensions()
    down_arrow_height = self.scroll_down_arrow.getWholeHeight()
    self.scroll_down_arrow.setPosition(0, own_dimensions.y - down_arrow_height)

  def getScrollPercentage(self):
    return self.scroll_percentage
  
  def setScrollPercentage(self, percentage):
    self.scroll_percentage = percentage
    self.scroll_frame.setVerticalScrollPercentage(percentage)

  def scrollToPercentage(self, percentage):
    if percentage < 0: percentage = 0
    if percentage > 100: percentage = 100
    self.setScrollPercentage(percentage)
    own_height = self.getHeight()
    knob_height = self.knob.getWholeHeight()
    up_arrow_height   = self.scroll_up_arrow.getWholeHeight()
    down_arrow_height = self.scroll_down_arrow.getWholeHeight()
    
    new_knob_position = Vector2D()
    new_knob_position.x = 0
    new_knob_position.y = mapRange(
      percentage,
      0, 100, 
      up_arrow_height, own_height - down_arrow_height - knob_height
    )
    self.knob.setPosition(0, new_knob_position.y)



class ScrollLeftArrow(Box):
  def __init__(self, horizontal_scrolls):
    Box.__init__(self)
    self.horizontal_scrolls = horizontal_scrolls
    self.setDimensions(11,11)
    self.setBorders(Pad(0,1,0,0))

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    # Draw a triangle arrow:
    left_co = (area.top_left.x + 2, area.top_left.y + 5)
    top_right_co = (area.top_left.x + 8, area.top_left.y + 2)
    bottom_right_co = (area.top_left.x + 8, area.top_left.y + 8)
    pygame.draw.polygon(surface, pygame.Color(0,0,0,255), [left_co, top_right_co, bottom_right_co])

  def onClick(self, event):
    old_percentage = self.horizontal_scrolls.getScrollPercentage()
    new_percentage = old_percentage - 10
    self.horizontal_scrolls.scrollToPercentage(new_percentage)

class ScrollRightArrow(Box):
  def __init__(self, horizontal_scrolls):
    Box.__init__(self)
    self.horizontal_scrolls = horizontal_scrolls
    self.setDimensions(11,11)
    self.setBorders(Pad(1,0,0,0))

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    # Draw a triangle arrow:
    right_co = (area.top_left.x + 8, area.top_left.y + 5)
    top_left_co = (area.top_left.x + 2, area.top_left.y + 2)
    bottom_left_co = (area.top_left.x + 2, area.top_left.y + 8)
    pygame.draw.polygon(surface, pygame.Color(0,0,0,255), [right_co, top_left_co, bottom_left_co])

  def onClick(self, event):
    old_percentage = self.horizontal_scrolls.getScrollPercentage()
    new_percentage = old_percentage + 10
    self.horizontal_scrolls.scrollToPercentage(new_percentage)

class HorizontalKnob(Box):
  def __init__(self, horizontal_scrolls):
    Box.__init__(self)
    self.horizontal_scrolls = horizontal_scrolls
  
    self.setWidth(30)
    self.setHeight(11)    

    self.setBorders(Pad(1,1,0,0))
    
    self.is_scrolling = False

  def onMouseButtonDown(self, event):
    if event.button == 1:
      self.is_scrolling = True

  def onMouseButtonUp(self, event):
    if event.button == 1:
      self.is_scrolling = False

  def onMouseOut(self, event):
    self.is_scrolling = False

  def onMouseMove(self, event):
    if self.is_scrolling:
      scrolls_width = self.horizontal_scrolls.getWidth()
      own_width = self.getWholeWidth()
      left_arrow_width  = self.horizontal_scrolls.scroll_left_arrow.getWholeWidth()
      right_arrow_width = self.horizontal_scrolls.scroll_right_arrow.getWholeWidth()
      
      mouse_rel_x = event.rel[0]
      own_pos = Vector2D(self.getPosition())
      own_pos.x += mouse_rel_x

      if own_pos.x < left_arrow_width: 
        own_pos.x = left_arrow_width
      if own_pos.x > scrolls_width - own_width - right_arrow_width: 
        own_pos.x = scrolls_width - own_width - right_arrow_width
  
      self.setPosition(own_pos)

      scroll_percentage = mapRange(
        own_pos.x, 
        left_arrow_width,  scrolls_width - right_arrow_width - own_width ,
        0, 100
      ) 

      self.horizontal_scrolls.setScrollPercentage(scroll_percentage )

  def draw(self, surface):
    Box.draw(self, surface)
    area = self.getContentArea()
    height = self.getHeight()
    width = self.getWidth()

    middle = round(width / 2.0)
    
    
    line1_co1 = (area.top_left.x + middle - 2, area.top_left.y + 2)
    line1_co2 = (area.top_left.x + middle - 2, area.top_left.y + height - 2)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line1_co1, line1_co2)

    line2_co1 = (area.top_left.x + middle, area.top_left.y + 2)
    line2_co2 = (area.top_left.x + middle, area.top_left.y + height - 2)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line2_co1, line2_co2)

    line3_co1 = (area.top_left.x + middle + 2, area.top_left.y +  2)
    line3_co2 = (area.top_left.x + width - 2 , area.top_left.y + middle + 2)
    line3_co2 = (area.top_left.x + middle + 2 , area.top_left.y + height - 2)
    pygame.draw.line(surface, pygame.Color(0,0,0,255), line3_co1, line3_co2)
    

class HorizontalScrolls(Frame):
  def __init__(self, scroll_frame):
    Frame.__init__(self)
    self.scroll_frame = scroll_frame
    self.scroll_percentage = 0

    self.setBorders(Pad(0,0,1,0))

    self.scroll_left_arrow = ScrollLeftArrow(self)
    self.scroll_right_arrow = ScrollRightArrow(self)
    self.knob = HorizontalKnob(self)
  
    Frame.addWidget(self, self.scroll_left_arrow)
    Frame.addWidget(self, self.scroll_right_arrow)
    Frame.addWidget(self, self.knob)
 
    self.setHeight(11)
     
  def layoutWidgets(self):
    Frame.layoutWidgets(self)
    left_arrow_width = self.scroll_left_arrow.getWholeWidth()
    self.knob.setPosition(left_arrow_width, 0)
    own_dimensions = self.getDimensions()
    right_arrow_width = self.scroll_right_arrow.getWholeWidth()
    self.scroll_right_arrow.setPosition(own_dimensions.x - right_arrow_width, 0)

  def getScrollPercentage(self):
    return self.scroll_percentage
  
  def setScrollPercentage(self, percentage):
    self.scroll_percentage = percentage
    self.scroll_frame.setHorizontalScrollPercentage(percentage)

  def scrollToPercentage(self, percentage):
    if percentage < 0: percentage = 0
    if percentage > 100: percentage = 100
    self.setScrollPercentage(percentage)
    own_width = self.getWidth()
    knob_width = self.knob.getWholeWidth()
    left_arrow_width  = self.scroll_left_arrow.getWholeWidth()
    right_arrow_width = self.scroll_right_arrow.getWholeWidth()
    
    new_knob_position = Vector2D()
    new_knob_position.y = 0
    new_knob_position.x = mapRange(
      percentage,
      0, 100, 
      left_arrow_width, own_width - right_arrow_width - knob_width
    )
    self.knob.setPosition(new_knob_position.x, 0)


class ScrollFrame(Frame):
  def __init__(self, scrolls = Scrolls.HORIZONTAL_AND_VERTICAL):
    Frame.__init__(self)
    
    self.horizontal_scroll_percentage = 0
    self.vertical_scroll_percentage   = 0

    self.inner_frame = Frame()
    self.inner_frame.setMargins(EqualPad(0))
    self.inner_frame.setBorders(EqualPad(0))
    self.inner_frame.setPaddings(EqualPad(0))
    self.inner_frame.setBorderDrawer(None)
    self.inner_frame.setBackgroundColor(Color(255,0,0))
    Frame.addWidget(self, self.inner_frame)

    self.horizontal_scrolls = None
    self.vertical_scrolls   = None
    if scrolls | Scrolls.VERTICAL:
      self.vertical_scrolls = VerticalScrolls(self)
    if scrolls | Scrolls.HORIZONTAL:
      self.horizontal_scrolls = HorizontalScrolls(self)

    if self.vertical_scrolls != None:
      Frame.addWidget(self, self.vertical_scrolls)
    if self.horizontal_scrolls != None:
      Frame.addWidget(self, self.horizontal_scrolls)


  def setLayout(self, layout):
    self.inner_frame.setLayout(layout)

  def setPaddings(self, paddings):
    self.inner_frame.setPaddings(paddings)

  def addWidget(self, widget):
    self.inner_frame.addWidget(widget)

  def removeWidget(self, widget):
    self.inner_frame.removeWidget(widget)

  def setDimensions(self, x, y = None):
    Frame.setDimensions(self, x,y)
    own_dimensions = self.getDimensions()
    
    horizontal_scrolls_height = self.horizontal_scrolls.getWholeHeight()
    vertical_scrolls_height  = own_dimensions.y - horizontal_scrolls_height
    
    vertical_scrolls_width = self.vertical_scrolls.getWholeWidth()
    horizontal_scrolls_width = own_dimensions.x - vertical_scrolls_width
      
    if self.vertical_scrolls != None and self.horizontal_scrolls == None: 
      vertical_scrolls_height = own_dimensions.y
    if self.vertical_scrolls == None and self.horizontal_scrolls != None:
      horizontal_scrolls_width = own_dimensions.x

    if self.vertical_scrolls != None:
      self.vertical_scrolls.setHeight(vertical_scrolls_height)
    if self.horizontal_scrolls != None:
      self.horizontal_scrolls.setWidth(horizontal_scrolls_width)
      
  def setVerticalScrollPercentage(self, percentage):
    self.vertical_scroll_percentage = percentage
    frame_height = self.inner_frame.getWholeHeight()
    own_height = self.getHeight() - self.horizontal_scrolls.getHeight()
      
    delta_height = frame_height - own_height
    if delta_height < 0: return
    scroll_amount = mapRange(self.vertical_scroll_percentage, 
      0, 100,
      0, -delta_height
    )
    inner_frame_pos = Vector2D(self.inner_frame.getPosition())
    inner_frame_pos.y = scroll_amount
    self.inner_frame.setPosition(inner_frame_pos)
  
  def setHorizontalScrollPercentage(self, percentage):
    self.horizontal_scroll_percentage = percentage
    frame_width = self.inner_frame.getWholeWidth()
    own_width = self.getWidth() - self.vertical_scrolls.getWidth()
  
    delta_width = frame_width - own_width
    if delta_width < 0: return
    scroll_amount = mapRange(self.horizontal_scroll_percentage,
      0, 100,
      0, -delta_width
    )
    inner_frame_pos = Vector2D(self.inner_frame.getPosition())
    inner_frame_pos.x = scroll_amount
    self.inner_frame.setPosition(inner_frame_pos)


  def layoutWidgets(self):
    own_dimensions = self.getDimensions()
    vertical_scrolls_width = self.vertical_scrolls.getWholeWidth()
    vertical_scrolls_left = own_dimensions.x - vertical_scrolls_width
    self.vertical_scrolls.setPosition(vertical_scrolls_left, 0)

    horizontal_scrolls_height = self.horizontal_scrolls.getWholeHeight()
    horizontal_scrolls_top = own_dimensions.y - horizontal_scrolls_height
    self.horizontal_scrolls.setPosition(0, horizontal_scrolls_top)


  def resizeToFit(self):
    return 