from .Widget import *
import pygame

# A simple box widget
class Box(Widget):
  def __init__(self, background_color, border_color):
    Widget.__init__(self)
    self.background_color = background_color
    self.border_color = border_color

  def draw(self, surface):
    
    