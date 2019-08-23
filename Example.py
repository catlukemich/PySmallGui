import random
import pygame
from gui.Input      import *
from gui.Gui        import *
from gui.Box        import *
from gui.Color      import *
from gui.Widget     import *
from gui.Container  import *
from gui.Frame      import *
from gui.GridLayout import *
from gui.HorizontalLayout import *
from gui.Layout      import *

def main():

  pygame.init()
  screen = pygame.display.set_mode((800,600))

  input = Input()
  
  gui = Gui(input)
  
  input.addMouseListener(gui)
  input.addKeyboardListener(gui)

  box = Box(Color(0,0,0),Color(255,0,0))
  box.setPosition(0,0)
  box.setDimensions(10,10)
  
  box.setPaddings(Pad(1, 2, 3, 4))
  box.setBorders(Pad(10, 10, 4, 4))
  box.setMargins(Pad(9, 10, 11, 12))
  
  
  container = Container()
  gui.addWidget(container)
  container.addWidget(box)

  content_area = box.getContentArea()
  padded_area = box.getPaddedArea()
  bordered_area = box.getBorderedArea()
  whole_area = box.getWholeArea()

  print "Content area: " + str(content_area)
  print "Padded area: " + str(padded_area)
  print "Bordered area: " + str(bordered_area)
  print "Whole area: " + str(whole_area) 

  # Testing parenting:
  frame = Frame()
  frame.setPosition(100,0)
  frame.setMargins(Pad(4,4,4,4))
  frame.setBorders(Pad(1,1,1,1))
  frame.setDimensions(219,200)
  #frame.setLayout(GridLayout(3,4))
  frame.setLayout(HorizontalLayout(Align.LEFT))
  gui.addWidget(frame)

  for i in range(0,8):
    
    box2 = Box()
    box2.setPosition(0,0)
    #size = 10 + random.randint(0,4)
    
    width = 20
    height = i * 5
    
    box2.setDimensions(width, height)
    box2.setBorders(Pad(1, 1, 1, 1))
    box2.setMargins(Pad(5, 5, 5 , 5))
    frame.addWidget(box2)

  # Testing clipping:
  frame = Frame()
  frame.setPosition(340,0)
  frame.setMargins(Pad(4,4,4,4))
  frame.setBorders(Pad(1,1,1,1))
  frame.setDimensions(80,200)
  gui.addWidget(frame)

  inner_frame = Frame()
  inner_frame.setPosition(40,0)
  inner_frame.setMargins(Pad(4,4,4,4))
  inner_frame.setBorders(Pad(1,1,1,1))
  inner_frame.setDimensions(180,100)
  frame.addWidget(inner_frame)
  
  inner_frame.setLayout(GridLayout(3,4))

  for i in range(0,12):
    col = i % 3
    row = i / 3
    
    box2 = Box()
    box2.setPosition(0,0)
    #size = 10 + random.randint(0,4)
    
    width = col * 10
    height = row * 5
    
    box2.setDimensions(width, height)
    box2.setBorders(Pad(1, 1, 1, 1))
    box2.setMargins(Pad(5, 5, 5 , 5))
    inner_frame.addWidget(box2)

  run = True
  while (run):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      input.handleEvent(event)
    

    screen.fill((255,255,255))
    gui.draw(screen)
    pygame.display.flip()


  pygame.quit()

if __name__ == "__main__":
  main()