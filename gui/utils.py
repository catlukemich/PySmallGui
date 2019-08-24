import random
import pygame

from .Font import Font
from .Font import Glyph

# Image loader functions
images = {}
def loadImage(path):
  global images
  if path in images:
    return images[path]
  else:
    img =  pygame.image.load(path).convert_alpha()
    images[path]= img
    return img

def loadFont(fnt_path, atlas_path):
  font_atlas = loadImage(atlas_path)

  font_ile = open(fnt_path, "r")
  contents = font_ile.read()
  lines = contents.split("\n")
  info_line = lines[0]
  font_size_column = info_line.split()[2]
  font_size = int(font_size_column.split("=")[1])
  print font_size

  start_line = 4
  glyphs = {}
  for line in range(start_line, len(lines)):
    line_text = lines[line]
    if not line_text.startswith("char"): break
    line_columns = line_text.split()
  
    print line_columns
    id_column = line_columns[1].strip()
    x_column = line_columns[2].strip()
    y_column = line_columns[3].strip()
    width_column  = line_columns[4].strip()
    height_column = line_columns[5].strip()
    xoffset_column = line_columns[6].strip()
    yoffset_column = line_columns[7].strip()
    xadvance_column = line_columns[8].strip()

    id = int(id_column.split("=")[1])
    x = int(x_column.split("=")[1])
    y = int(y_column.split("=")[1])
    width = int(width_column.split("=")[1])
    height = int(height_column.split("=")[1])
    x_offset = int(xoffset_column.split("=")[1])
    y_offset = int(yoffset_column.split("=")[1])
    xadvance = int(xadvance_column.split("=")[1]) 

    glyphs[id] = Glyph(id, x, y, width, height, x_offset, y_offset, xadvance)
    
  return Font(font_size, glyphs, font_atlas)
