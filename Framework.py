import random
import pygame

import gui

from gui.Pad import Pad
from gui.Pad import EqualPad
from gui.Alignment import Align


class Framework():

  def main(self):

    pygame.init()
    screen = pygame.display.set_mode((1200,1000))

    input = gui.Input()
    
    the_gui = gui.Gui(input)
    
    input.addMouseListener(the_gui)
    input.addKeyboardListener(the_gui)

    self.init(the_gui)

    run = True
    while (run):
      event_consumed = False
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        else:
          event_consumed = input.handleEvent(event)
          if not event_consumed:
            pass # The gui didn't consumed the event, process the event as you like.
          else: print "Event consumed"
      

      screen.fill((255,255,255))
      the_gui.draw(screen)
      pygame.display.flip()


    pygame.quit()

  def init(self, the_gui):
    pass

