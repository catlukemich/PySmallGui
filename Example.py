import pygame
from gui.Input      import *
from gui.Gui        import *
from gui.Box        import *
from gui.Color      import *
from gui.Widget     import *
from gui.Container  import *
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
  container.setPosition(100,100)
  gui.addWidget(container)
  container.addWidget(box)


  content_area = box.getContentArea()
  padded_area = box.getPaddedArea()
  bordered_area = box.getBorderedArea()
  whole_area = box.getWholeArea()

  print "Content area: " + str(content_area) # should be 6, 6 to 16, 16
  print "Padded area: " + str(padded_area) # should be 
  print "Bordered area: " + str(bordered_area)
  print "Whole area: " + str(whole_area) # should be 0,0 to 43, 55

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