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
  def getAlignmentOffset(width_outer, height_outer, width_inner, height_inner, align = Align.CENTER):
    # Calculate the top offset and left  offset:
    offset_left = (width_outer - width_inner) / 2.0
    offset_top = (height_outer - height_inner) / 2.0
    if align == Align.CENTER:
      pass
    elif align == Align.LEFT:
      offset_left = 0
    elif align == Align.RIGHT:
      offset_left = width_outer - width_inner
    elif align == Align.TOP:
      offset_top = 0
    elif align == Align.BOTTOM:
      offset_top = height_outer - height_inner
    elif align == Align.TOP_LEFT:
      offset_left = 0
      offset_top = 0
    elif align == Align.TOP_RIGHT:
      offset_left = width_outer - width_inner
      offset_top = 0
    elif align == Align.BOTTOM_LEFT:
      offset_left = 0
      offset_top = height_outer - height_inner
    elif align == Align.BOTTOM_RIGHT:
      offset_left = width_outer - width_inner
      offset_top = height_outer - height_inner

    return Vector2D(round(offset_left), round(offset_top))
    