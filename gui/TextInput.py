import pygame

from .Vector2D import Vector2D
from .Box import Box
from .Label import Label
from .BackgroundDrawer import BackgroundDrawer
from .BorderDrawer import BorderDrawer
from .Frame import Frame

class TextInput(Label):
  def __init__(self, width, font, text = ""):
    Label.__init__(self, font, text)
    self.setWidth(width)
    self.setHeight(font.size)
    
    self.caret_index = 0
    self.caret = self.createCaret()

    self.setBackgroundDrawer(BackgroundDrawer())
    self.setBorderDrawer(BorderDrawer())

    self.has_focus = False

  def createCaret(self):
    width = 2
    height = self.font.size
    caret = pygame.Surface((width, height))
    caret.fill((0,0,0,255))
    pygame.draw
    return caret

  def onMouseButtonDown(self, event): 
    if self.text.strip() == False:
      return

    mouse = Vector2D(event.pos[0], event.pos[1])
    content_area = self.getContentArea()
    offset_left = content_area.top_left.x
    current_x = 0

    for letter_index in range(0, len(self.text) ):
      text_current = self.text[0:letter_index]
      width_current = self.getTextWidth(text_current)
      text_next = self.text[0:letter_index+1]
      width_next = self.getTextWidth(text_next)
      if mouse.x >= width_current + offset_left and mouse.x <= width_next + offset_left :
        self.caret_index = letter_index
        break

  def onKeyDown(self, event):
    
    if (event.key >= 65 and event.key <= 90) or (event.key >= 97 and event.key <= 122) or event.key == 32:
      char = chr(event.key)
      if event.key >= 96 and event.key <= 122:
        if event.mod == 2:
          char = chr(event.key - 32) # Big letter
      if event.key == 32: char = " "
      text_before = self.text[0:self.caret_index]
      text_before += char 
      text_after  = self.text[self.caret_index:]
      self.text = text_before + text_after

      self.text_surface = self.drawTextSurface()
      self.caret_index += 1
    
    else:
      if event.key == 276: # Arrow left
        self.caret_index -= 1
      if event.key == 275: # Arrow right
        self.caret_index += 1
      if event.key == 8: # Backspace
        text_before = self.text[0:self.caret_index - 1]
        text_after  = self.text[self.caret_index:]
        self.text = text_before + text_after
        self.text_surface = self.drawTextSurface()  
        self.caret_index -= 1
      if event.key == 127: # Delete
        text_before = self.text[0:self.caret_index ]
        text_after  = self.text[self.caret_index + 1:]
        self.text = text_before + text_after
        self.text_surface = self.drawTextSurface()  
      
    if self.caret_index < 0:
      self.caret_index = 0
    if self.caret_index > len(self.text):
      self.caret_index = len(self.text)
      

  def onFocusGain(self, event):
    self.has_focus = True

  def onFocusLost(self, event):
    self.has_focus = False

  def draw(self, surface):
    # Draw the background and the border:
    bg_drawer = self.getBackgroundDrawer()
    border_drawer = self.getBorderDrawer()
    bg_drawer.drawBackground(self, surface)
    border_drawer.drawBorder(self, surface)
  
    # Do the clipping of the text:
    orig_clip = surface.get_clip()
    clip = self.getContentArea()
    
    parent = self.getParent()
    if(isinstance(parent, Frame)):
      parent_clip = parent.getClippingRectangle()
      clip = parent_clip.intersection(clip)
  
    surface.set_clip(pygame.Rect(
      clip.top_left.x, clip.top_left.y, 
      clip.bottom_right.x - clip.top_left.x, clip.bottom_right.y - clip.top_left.y)
    )

    # Draw the text:
    content_area = self.getContentArea()
    surface.blit(self.text_surface, (content_area.top_left.x, content_area.top_left.y))

    # Draw the caret if the widget has focus:
    if self.has_focus:
      text_before = self.text[0:self.caret_index]
      content_area = self.getContentArea()
      caret_position_left = self.getTextWidth(text_before) + content_area.top_left.x 
      caret_position_top = content_area.top_left.y 
      surface.blit(self.caret, (caret_position_left, caret_position_top))
    
    # Reset the clip:
    surface.set_clip(orig_clip)