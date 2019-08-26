import random
import pygame

import gui

from gui.Pad import Pad
from gui.Pad import EqualPad
from gui.Alignment import Align


class Framework():

  def main(self):

    pygame.init()
    screen = pygame.display.set_mode((800,600))

    input = gui.Input()
    
    the_gui = gui.Gui(input)
    
    input.addMouseListener(the_gui)
    input.addKeyboardListener(the_gui)

    self.init(the_gui)

    run = True
    while (run):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        input.handleEvent(event)
      

      screen.fill((255,255,255))
      the_gui.draw(screen)
      pygame.display.flip()


    pygame.quit()

  def init(self, the_gui):
    pass

