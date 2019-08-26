import pygame
from .Box import Box
from .Vector2D import Vector2D

class Label(Box):
  def __init__(self, font, text = ""):
    Box.__init__(self)
    self.font = font
    self.text = text
    
    self.text_surface = self.drawTextSurface()
    size = self.text_surface.get_size()
    self.setDimensions(size[0], size[1])

    self.setBorderDrawer(None)
    self.setBackgroundDrawer(None)

  def setText(self, text):
    self.text = text
    self.text_surface = self.drawTextSurface()
    size = self.text_surface.get_size()
    self.setDimensions(size[0], size[1])
  
  def getText(self):
    return self.text

  def getTextWidth(self, text):
    width = 0
    for letter in text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      width += glyph.xadvance
    return width

  def drawTextSurface(self):
    height = self.font.size
    width = self.getTextWidth(self.text)
    
    text_surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        
    current_width = 0
    for letter in self.text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      top = 0
      
      area = pygame.Rect(glyph.x, glyph.y, glyph.width, glyph.height)
      text_surface.blit(self.font.atlas, 
        (current_width + glyph.x_offset, top + glyph.y_offset), 
        area
      )

      current_width += glyph.xadvance
    
    return text_surface

  def draw(self, surface):
    Box.draw(self, surface)
    content_area = self.getContentArea()
    surface.blit(self.text_surface, (content_area.top_left.x, content_area.top_left.y))