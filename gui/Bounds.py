from .Vector2D import *

  
class Bounds():
  def __init__(self, top_left = Vector2D(0,0) , bottom_right = Vector2D(0, 0)):
    self.top_left = top_left
    self.bottom_right = bottom_right

  def containsPoint(self, x, y = None):
    point = None
    if isinstance(x, Vector2D):
      point = x
    else: 
      point = Vector2D(x, y)

    return self.top_left < point and point < self.bottom_right

  # Get the intersection of two Bounds objects. 
  def intersection(self, other):
    top_left_x = max(self.top_left.x, other.top_left.x)
    top_left_y = max(self.top_left.y, other.top_left.y)
    bottom_right_x = min(self.bottom_right.x, other.bottom_right.x)
    bottom_right_y = min(self.bottom_right.y, other.bottom_right.y)
    
    top_left = Vector2D(top_left_x, top_left_y)
    bottom_right = Vector2D(bottom_right_x, bottom_right_y)

    if bottom_right < top_left: return Bounds() # Return empty bounds
    else: return Bounds(top_left, bottom_right)

  def __str__(self):
    return "Bounds, top left: %s, bottom_right: %s" % (self.top_left, self.bottom_right)

