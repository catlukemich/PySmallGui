import pygame
from .Box import Box
from .Vector2D import Vector2D
from .Color import Color

class Label(Box):
  def __init__(self, font, text = ""):
    Box.__init__(self)
    self.font = font
    self.text = text
    
    self.color = Color(0,0,0)

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
  
  def setTextColor(self, color):
    self.color = color
    self.text_surface = self.drawTextSurface()

  def getText(self):
    return self.text

  def getTextWidth(self, text):
    width = 0
    for letter in text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      width += int(glyph.xadvance)
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
    
    text_surface.fill(
      (self.color.red, self.color.green, self.color.blue), 
      None, pygame.BLEND_RGBA_MULT
    )

    return text_surface

  def draw(self, surface):
    Box.draw(self, surface)
    content_area = self.getContentArea()
    surface.blit(self.text_surface, (content_area.top_left.x, content_area.top_left.y))