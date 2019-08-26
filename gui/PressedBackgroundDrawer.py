import pygame

from .BackgroundDrawer import *

class PressedBackgroundDrawer(BackgroundDrawer):
  def __init__(self, bg_color = Color(240,240,240), shadow_color = Color(220,220,220)):
    BackgroundDrawer.__init__(self, bg_color)
    self.shadow_color = shadow_color

  def drawBackground(self, widget, surface):
    BackgroundDrawer.drawBackground(self, widget, surface)
    padded_area = widget.getPaddedArea()
    pygame_color = pygame.Color(self.shadow_color.red, self.shadow_color.green, self.shadow_color.blue, self.shadow_color.alpha)
    
    # Draw the left shadow:
    start_x = padded_area.top_left.x
    end_x = start_x + 2
    start_y = padded_area.top_left.y
    end_y = padded_area.bottom_right.y
    width = end_x - start_x
    height = end_y - start_y
    
    draw_rect = pygame.Rect(start_x, start_y, width, height)
    pygame.draw.rect(surface, pygame_color, draw_rect)

    # Draw the top shadow:
    start_x = padded_area.top_left.x
    end_x = padded_area.bottom_right.x
    start_y = padded_area.top_left.y
    end_y = start_y + 2
    width = end_x - start_x
    height = end_y - start_y

    draw_rect = pygame.Rect(start_x, start_y, width, height)
    pygame.draw.rect(surface, pygame_color, draw_rect)
    