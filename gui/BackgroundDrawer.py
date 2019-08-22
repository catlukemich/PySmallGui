from .Vector2D import *
import pygame

# A base background drawer class. Draws a simple solid background.
class BackgroundDrawer():
  def drawBackground(self, widget, surface, color):
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
    
    pygame_color = pygame.Color(color.red, color.green, color.blue, color.alpha)
    pygame.draw.rect(surface, pygame_color, background_rect )
