from .Frame import Frame
from .Label import Label
from .VerticalLayout import VerticalLayout
from .BackgroundDrawer import BackgroundDrawer
from .BorderDrawer import BorderDrawer
from .Color import Color
from .Pad import Pad


class LabelFrame(Frame):
  def __init__(self, font, label_text = ""):
    Frame.__init__(self)
    Frame.setLayout(self, VerticalLayout())
    
    self.label = Label(font, label_text)
    self.label.setTextColor(Color(255,255,255))
    self.label.setBackgroundDrawer(BackgroundDrawer())
    self.label.setBackgroundColor(Color(0,0,0))
    self.label.setBorderDrawer(BorderDrawer())
    self.label.setBorders(Pad(0,0,0,1))
    Frame.addWidget(self, self.label)

    self.inner_frame = Frame()
    self.inner_frame.setBorders(Pad(0,0,0,0))
    self.inner_frame.setBackgroundDrawer(None)
    self.inner_frame.setBorderDrawer(None)
    Frame.addWidget(self, self.inner_frame)
  
  def setLabelPaddings(self, paddings):
    self.label.setPaddings(paddings)

  def setLayout(self, layout):
    self.inner_frame.setLayout(layout)
    self.resizeLabel()

  def setPaddings(self, paddings):
    self.inner_frame.setPaddings(paddings)
    self.resizeLabel()

  def setLabelText(self, text):
    self.label.setText(text)
    self.resizeLabel()

  def addWidget(self, widget):
    self.inner_frame.addWidget(widget)
    self.resizeLabel()

  def removeWidget(self, widget):
    self.inner_frame.removeWidget(widget)
    self.resizeLabel()

  def resizeLabel(self):
    paddings = self.label.getPaddings()
    width = self.layout.getWidth(self) - paddings.left - paddings.right
    self.label.setWidth(width)