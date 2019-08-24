class Glyph():
  def __init__(self, id, x, y, width, height, x_offset, y_offset, xadvance):
    self.id = id
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.x_offset = x_offset
    self.y_offset = y_offset
    self.xadvance = xadvance

class Font():
  def __init__(self, size, glyphs, atlas):
    self.size = size
    self.glyphs = glyphs  
    self.atlas = atlas

  def getGlyph(self, id):
    return self.glyphs[id]