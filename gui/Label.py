import pygame
from .Box import Box

class Label(Box):
  def __init__(self, font, text = ""):
    Box.__init__(self)
    self.font = font
    self.text = text
    self.drawTextSurface()

  def drawTextSurface(self):
    height = self.font.size
    width = 0
    for letter in self.text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      width += glyph.xadvance
    
    text_surface = pygame.Surface((width, height))
    print "h,w :" + str(height) + " " + str(width)

    current_width = 0
    for letter in self.text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      current_width += glyph.xadvance
      top = 0
      
      text_surface.blit(font.atlas, (current_width, top), )
    

  def draw(self, surface):
    Box.draw(self, surface)
    