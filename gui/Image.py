from .Box import *
import pygame

class Image(Box):
  def __init__(self, image):
    Box.__init__(self)
    self.original_image = image
    self.transformed_image = image


  def setImage(self, image):
    self.original_image = image
    self.transformImage()

  def setDimensions(self, x, y):
    Box.setDimensions(self, x, y)
    self.transformImage()

  def transformImage(self):
    dims = self.getDimensions()
    self.transformed_image = pygame.transform.scale(self.original_image, (dims.x, dims.y))
    

  
  

  def draw(self, surface):
    Box.draw(self, surface)
    content_area = self.getContentArea()
    surface.blit(
      self.transformed_image, 
      (content_area.top_left.x, content_area.top_left.y))
    