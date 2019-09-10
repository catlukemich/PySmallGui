from .Image import *
from .Color import *
from .PressedBackgroundDrawer import *
from .PressedBorderDrawer     import *

class ImageButton(Image):

  def __init__(self, default_image, pressed_image = None):
    self.default_image = default_image
    if pressed_image == None: 
      pressed_image = default_image
    self.pressed_original_image = pressed_image
    self.pressed_transformed_image = pressed_image
    
    Image.__init__(self, default_image)

    self.released_background_drawer = self.getBackgroundDrawer()
    self.released_border_drawer = self.getBorderDrawer()

    self.pressed_background_drawer = PressedBackgroundDrawer()
    self.pressed_border_drawer = PressedBorderDrawer()
    
    

  # Set the image that is displayed when the mouse button is pressed:
  def setPressedImage(self, pressed_image):
    self.pressed_original_image = pressed_image
    self.transformImage()

  def transformImage(self):
    Image.transformImage(self)
    dims = self.getDimensions()
    self.pressed_transformed_image = pygame.transform.scale(self.pressed_original_image, (dims.x, dims.y))
    

  def onMouseButtonDown(self, event):
    self.setImage(self.pressed_original_image)
    self.setBackgroundDrawer(self.pressed_background_drawer)
    self.setBorderDrawer(self.pressed_border_drawer)
    

  def onMouseButtonUp(self, event): 
    self.setImage(self.default_image)
    self.setBackgroundDrawer(self.released_background_drawer)
    self.setBorderDrawer(self.released_border_drawer)

  def onMouseOut(self, event):
    Image.onMouseOut(self, event)
    self.setImage(self.default_image)
    self.setBackgroundDrawer(self.released_background_drawer)
    self.setBorderDrawer(self.released_border_drawer)