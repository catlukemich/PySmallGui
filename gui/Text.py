import pygame

from .Box import Box
from .Alignment import Align
from .Alignment import Aligner

class Line():
  def __init__(self, width, text):
    self.width = width
    self.text = text

  def __str__(self):
    return "Line: width: %d, contents: %s" % (self.width, self.text) 

class Text(Box):
  def __init__(self, font, text = ""):
    Box.__init__(self)
    
    self.font = font
    self.text = text

    #self.setBackgroundDrawer(None)
    #self.setBorderDrawer(None)

    self.text_align = Align.CENTER

    self.text_surface = self.drawTextSurface()
    
  def getTextWidth(self, text):
    width = 0
    for letter in text:
      id = ord(letter)
      glyph = self.font.getGlyph(id)
      width += glyph.xadvance
    return width


  def setText(self, text):
    self.text = text
    self.text_surface = self.drawTextSurface()

  def setTextAlign(self, align):
    self.text_align = align
  
  def drawTextSurface(self):
    lines = []
    words = self.text.split()

    current_x = 0
    current_y = 0
    
    current_text = ""
  
    dimensions = self.getDimensions()

    for word_idx in range(0, len(words) ):
      current_word = words[word_idx]
      current_word_width = self.getTextWidth(current_word + " ")
      current_text += current_word + " "
      next_word = None
      next_word_width = 0
      current_x += current_word_width
      try: 
        next_word = words[word_idx + 1]
        next_word_width = self.getTextWidth(next_word)
      except: pass
      if current_x + next_word_width  > dimensions.x:
        lines.append(Line(current_x, current_text))
        current_x = 0
        current_text = ""
      current_y += self.font.size

    lines.append(Line(current_x, current_text))

    surf_width = 0
    surf_height = 0 
    for line in lines:
      if line.width > surf_width: surf_width = line.width
      surf_height += self.font.size
    

    text_surface = pygame.Surface((surf_width, surf_height), pygame.SRCALPHA, 32).convert_alpha()
    
    current_y = 0
    for line in lines:
      current_x = 0

      offset_vector = Aligner.getAlignmentPosition(surf_width, 0 , line.width, 0, self.text_align)
      for letter in line.text:
        id = ord(letter)
        glyph = self.font.getGlyph(id)
        
        text_surface.blit(self.font.atlas, 
          (current_x + glyph.x_offset + offset_vector.x, current_y + glyph.y_offset), 
          pygame.Rect(glyph.x, glyph.y, glyph.width, glyph.height)
        )
        current_x += glyph.xadvance

      current_x = 0
      current_y += self.font.size
    
    return text_surface

  def draw(self, surface):
    Box.draw(self, surface)

    dimensions = self.getDimensions()
    surface_size = self.text_surface.get_size()
    surface_offset = Aligner.getAlignmentPosition(dimensions.x, dimensions.y, surface_size[0], surface_size[1], self.text_align)


    content_area = self.getContentArea()
    surface.blit(self.text_surface, (content_area.top_left.x + surface_offset.x, content_area.top_left.y + surface_offset.y))