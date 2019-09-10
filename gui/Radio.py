import pygame

from .Frame import Frame
from .GridLayout import GridLayout
from .Box import Box
from .Label import Label

class RadioButton(Box):
  def __init__(self, radio):
    Box.__init__(self)
    self.radio = radio
    self.selected = False

    self.setDimensions(10, 10)

    self.setBackgroundDrawer(None)
    self.setBorderDrawer(None)


  def setSelected(self, selected):
    self.selected = selected

  def isSelected(self):
    return self.selected

  def onClick(self, event):
    self.radio.deselectAll()
    self.setSelected(True)
    Box.onClick(self, event)

  def draw(self, surface):
    content_area = self.getContentArea()
    center_x = int(content_area.top_left.x + 5)
    center_y = int(content_area.top_left.y + 5)

    # Draw the outer circle:
    pygame.draw.circle(surface, (0, 0, 0), (center_x, center_y), 5, 1 )

    # Draw the inner circle if selected:
    if self.selected:
      pygame.draw.circle(surface, (0,0,0), (center_x, center_y), 2)



class Radio(Frame):
  def __init__(self, font):
    Frame.__init__(self)
    self.font = font
    self.setLayout(GridLayout(2,2))
    self.options = {}

    self.setBackgroundDrawer(None)
    self.setBorderDrawer(None)

  def addOption(self, value, text):
    label = Label(self.font, text)
    radiobutton = RadioButton(self)
    self.options[value] = (radiobutton, label)

    rows = len(self.options)
    self.setLayout(GridLayout(2, rows))

    self.addWidget(radiobutton)
    self.addWidget(label)

  def deselectAll(self):
    for value in self.options:
      radio_tuple = self.options[value]
      radiobutton = radio_tuple[0]
      radiobutton.setSelected(False)

  def getSelected(self):
    selected = None
    for value in self.options:
      radio_tuple = self.options[value]
      radiobutton = radio_tuple[0]
      is_selected = radiobutton.isSelected()
      if is_selected: selected = value

    return selected

  def addListener(self, listener):
    for value in self.options:
      radio_tuple = self.options[value]
      radiobutton = radio_tuple[0]
      radiobutton.addListener(listener)


  def removeListener(self, listener):
    for value in self.options:
      radio_tuple = self.options[value]
      radiobutton = radio_tuple[0]
      radiobutton.removeListener(listener)