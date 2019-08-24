class Pad():
  def __init__(self, left = 0, right = 0, top = 0, bottom = 0):
    self.left   = left
    self.right  = right
    self.top    = top
    self.bottom = bottom

  def __str__(self):
    return "Pad, left: %d, right: %d, top: %d, bottom: %d" % (self.left, self.right, self.top, self.bottom)

class EqualPad(Pad):
  def __init__(self, pad):
    Pad.__init__(self, pad, pad, pad, pad)
