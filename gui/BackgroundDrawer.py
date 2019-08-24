from .Vector2D import *
from .Color import *
import pygame

# A base background drawer class. Draws a simple solid background.
class BackgroundDrawer():

  def __init__(self, color = Color(240,240,240)):
    self.color = color

  def drawBackground(self, widget, surface):
    absolute_position = widget.calcAbsolutePosition()

    margin = widget.getMargins()
    border = widget.getBorders()
    padding = widget.getPaddings()
    dimensions = widget.getDimensions()

    # Drawing background:
    background_top_left = Vector2D(
      absolute_position.x + margin.left + border.left, 
      absolute_position.y + margin.top + border.top)
    background_bottom_right = Vector2D(
      absolute_position.x + margin.left + border.left + padding.left + dimensions.x + padding.right ,
      absolute_position.y + margin.top + border.top + padding.top + dimensions.y + padding.bottom , )
    
    draw_width = background_bottom_right.x - background_top_left.x
    draw_height = background_bottom_right.y - background_top_left.y

    background_rect = pygame.Rect(background_top_left.x, background_top_left.y, draw_width, draw_height)
    
    pygame_color = pygame.Color(self.color.red, self.color.green, self.color.blue, self.color.alpha)
    pygame.draw.rect(surface, pygame_color, background_rect )
