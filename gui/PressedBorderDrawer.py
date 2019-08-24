from .Color import Color
from .BorderDrawer import BorderDrawer

class PressedBorderDrawer(BorderDrawer):
  def __init__(self, color = Color(255, 0, 0)):
    BorderDrawer.__init__(self, color)