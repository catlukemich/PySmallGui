import pygame


class MouseListener:
  def mouseButtonDown(self, event):
    pass
    
  def mouseButtonUp(self, event):
    pass

  def mouseMotion(self, event):
    pass

  def mouseWheel(self, event):
    pass
    
class KeyboardListener:
  def keyDown(self, event):
    pass
    
  def keyUp(self,event):
    pass
    
class Input:
  def __init__(self):
    self.key_listeners   = []
    self.mouse_listeners = []
    
    
  def addMouseListener(self, listener):
    self.mouse_listeners.append(listener)
    
  def addKeyboardListener(self, listener):
    self.key_listeners.append(listener)
    
    
  
  def handleEvent(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 or event.button == 2 or event.button == 3) :
      for listener in self.mouse_listeners:
        consumed = listener.mouseButtonDown(event)
        if consumed: 
          break
    
    if event.type == pygame.MOUSEBUTTONUP:
      for listener in self.mouse_listeners:
        consumed = listener.mouseButtonUp(event)
        if consumed: 
          break
    
    if event.type == pygame.MOUSEMOTION:
      for listener in self.mouse_listeners:
        consumed = listener.mouseMotion(event)
        if consumed: 
          break
    
    # Mouse wheel event is when the event type is MOUSEBUTTONDOWN and the button is 4 or 5
    if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button == 5):
      for listener in self.mouse_listeners:
        consumed = listener.mouseWheel(event)
        if consumed: 
          break 
    
    if event.type == pygame.KEYDOWN:
      for listener in self.key_listeners:
        consumed = listener.keyDown(event)
        if consumed: 
          break
          
    if event.type == pygame.KEYUP:
      for listener in self.key_listeners:
        consumed = listener.keyUp(event)
        if consumed: 
          break
    