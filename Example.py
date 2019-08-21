import pygame
from gui.Input import *
from gui.Gui import *

def main():

  pygame.init()
  screen = pygame.display.set_mode((800,600))

  input = Input()
  
  gui = Gui()
  
  input.addMouseListener(gui)
  input.addKeyboardListener(gui)

  run = True
  while (run):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      input.handleEvent(event)
    

    screen.fill((255,255,255))
    pygame.display.flip()


  pygame.quit()

if __name__ == "__main__":
  main()