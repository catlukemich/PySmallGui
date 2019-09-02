from .Vector2D import *
from .Color import *
import pygame

class BorderDrawer():

  def __init__(self, color = Color(150,150,150)):
    self.color = color


  def setColor(self, color):
    self.color = color

  def drawBorder(self, widget, surface):
    absolute_position = widget.calcAbsolutePosition()

    bordered_area = widget.getBorderedArea()
    outer_top_left = bordered_area.top_left
    outer_bottom_right = bordered_area.bottom_right

    padded_area = widget.getPaddedArea()
    inner_top_left = padded_area.top_left
    inner_bottom_right = padded_area.bottom_right


    # Drawing borders:
    pygame_color = pygame.Color(self.color.red, self.color.green, self.color.blue, self.color.alpha)

    # Left border:
    border_left_top_left = outer_top_left
    border_left_bottom_right = Vector2D(inner_top_left.x , outer_bottom_right.y)

    border_left_width  = border_left_bottom_right.x - border_left_top_left.x
    border_left_height = border_left_bottom_right.y - border_left_top_left.y

    border_left_rect = pygame.Rect(
      border_left_top_left.x, border_left_top_left.y, 
      border_left_width, border_left_height)

    if not(border_left_width == 0 or border_left_height == 0):
      pygame.draw.rect(surface, pygame_color, border_left_rect )

    
    # Right border:
    border_right_top_left = Vector2D(inner_bottom_right.x, outer_top_left.y)
    border_right_bottom_right = outer_bottom_right
    
    border_right_width  = border_right_bottom_right.x - border_right_top_left.x
    border_right_height = border_right_bottom_right.y - border_right_top_left.y

    border_right_rect = pygame.Rect(
      border_right_top_left.x, border_right_top_left.y, 
      border_right_width, border_right_height)
    
    if not(border_right_width == 0 or border_right_height == 0):
      pygame.draw.rect(surface, pygame_color, border_right_rect )

    # Top border:
    border_top_top_left = outer_top_left
    border_top_bottom_right = Vector2D(outer_bottom_right.x, inner_top_left.y)
    
    border_top_width  = border_top_bottom_right.x - border_top_top_left.x
    border_top_height = border_top_bottom_right.y - border_top_top_left.y

    border_top_rect = pygame.Rect(
      border_top_top_left.x, border_top_top_left.y, 
      border_top_width, border_top_height)
    
    if not(border_top_width == 0 or border_top_height == 0):
      pygame.draw.rect(surface, pygame_color, border_top_rect )


    # Bottom border:  
    border_bottom_top_left = Vector2D(outer_top_left.x, inner_bottom_right.y)
    border_bottom_bottom_right = outer_bottom_right
    
    border_bottom_width  = border_bottom_bottom_right.x - border_bottom_top_left.x
    border_bottom_height = border_bottom_bottom_right.y - border_bottom_top_left.y

    border_bottom_rect = pygame.Rect(
      border_bottom_top_left.x, border_bottom_top_left.y, 
      border_bottom_width, border_bottom_height)
    
    if not(border_bottom_width == 0 or border_bottom_height == 0):
      pygame.draw.rect(surface, pygame_color, border_bottom_rect )

