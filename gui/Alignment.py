from .Vector2D import Vector2D

class Align():
  CENTER = 0

  LEFT    = 1
  RIGHT   = 2
  TOP     = 3
  BOTTOM  = 4
  
  TOP_LEFT      = 5
  TOP_RIGHT     = 6
  BOTTOM_LEFT   = 7
  BOTTOM_RIGHT  = 8


class Aligner():

  @staticmethod
  def getAlignmentPosition(width_outer, height_outer, width_inner, height_inner, align = Align.CENTER):
   

    # Calculate the top bounds offset and left bounds offset:
    bounds_offset_left = (width_outer - width_inner) / 2
    bounds_offset_top = (height_outer - height_inner) / 2
    if align == Align.CENTER:
      pass
    elif align == Align.LEFT:
      bounds_offset_left = 0
    elif align == Align.RIGHT:
      bounds_offset_left = width_outer - width_inner
    elif align == Align.TOP:
      bounds_offset_top = 0
    elif align == Align.BOTTOM:
      bounds_offset_top = height_outer - height_inner
    elif align == Align.TOP_LEFT:
      bounds_offset_left = 0
      bounds_offset_top = 0
    elif align == Align.TOP_RIGHT:
      bounds_offset_left = width_outer - width_inner
      bounds_offset_top = 0
    elif align == Align.BOTTOM_LEFT:
      bounds_offset_left = 0
      bounds_offset_top = height_outer - height_inner
    elif align == Align.BOTTOM_RIGHT:
      bounds_offset_left = width_outer - width_inner
      bounds_offset_top = height_outer - height_inner

    return Vector2D(bounds_offset_left, bounds_offset_top)
    