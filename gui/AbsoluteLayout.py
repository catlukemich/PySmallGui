from .Layout import *
import sys

class AbsoluteLayout(Layout):
  def getWidth(self, parent):
    dimensions = parent.getDimensions()
    return dimensions.x


  def getHeight(self, parent):
    dimensions = parent.getDimensions()
    return dimensions.y