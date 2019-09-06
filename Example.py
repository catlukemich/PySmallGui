import random
import pygame

import gui

from gui.Pad import Pad
from gui.Pad import EqualPad
from gui.Alignment import Align

def main():

  pygame.init()
  screen = pygame.display.set_mode((800,600))


  input = gui.Input()
  
  the_gui = gui.Gui(input)
  
  input.addMouseListener(the_gui)
  input.addKeyboardListener(the_gui)
  


  box = gui.Box()
  box.setPosition(0,0)
  box.setDimensions(10,10)
  
  box.setPaddings(Pad(1, 2, 3, 4))
  box.setBorders(Pad(10, 10, 4, 4))
  box.setMargins(Pad(9, 10, 11, 12))
  
  
  container = gui.Container()
  the_gui.addWidget(container)
  container.addWidget(box)


  content_area = box.getContentArea()
  padded_area = box.getPaddedArea()
  bordered_area = box.getBorderedArea()
  whole_area = box.getWholeArea()

 

  # Testing parenting:
  frame = gui.Frame()
  frame.setPosition(0,0)
  #frame.setMargins(EqualPad(4))
  frame.setBorders(EqualPad(1))
  frame.setPaddings(Pad(2,2,20,2))
  frame.setDimensions(200,200)
  #frame.setLayout(gui.GridLayout(3,4))
  #frame.setLayout(gui.GridLayout(2, 4, Align.TOP))
  frame.setLayout(gui.VerticalLayout())
  the_gui.addWidget(frame)
  
 

  for i in range(0,8):
    
    box = gui.Box()
    box.setPosition(0,0)
    #size = 10 + random.randint(0,4)
    
    width = i * 5
    height = i * 5
    
    box.setBorders(Pad(1, 1, 1, 1))
    box.setMargins(Pad(5, 5, 5 , 5))
    frame.addWidget(box)
    box.setDimensions(width, height)


 

  # Testing clipping:
  frame = gui.Frame()
  frame.setPosition(340,0)
  
  frame.setMargins(Pad(4,4,4,4))
  frame.setBorders(Pad(1,1,1,1))
  frame.setDimensions(80,200)
  frame.setPaddings(EqualPad(15))
  the_gui.addWidget(frame)

  inner_frame = gui.Frame()
  inner_frame.setPosition(40,0)
  inner_frame.setMargins(Pad(4,4,4,4))
  inner_frame.setBorders(Pad(1,1,1,1))
  inner_frame.setDimensions(180,100)
  frame.addWidget(inner_frame)
  
  inner_frame.setLayout(gui.GridLayout(3,5))

  for i in range(0,12):
    col = i % 3
    row = i / 3
    
    box2 = gui.Box()
    box2.setPosition(0,0)
    #size = 10 + random.randint(0,4)
    
    width = col * 10
    height = row * 5
    
    box2.setDimensions(width, height)
    box2.setBorders(Pad(1, 1, 1, 1))
    box2.setMargins(Pad(5, 5, 5 , 5))
    inner_frame.addWidget(box2)

  img = gui.loadImage("res/aircraft.png")
  image_widget = gui.Image(img)
  image_widget.setPosition(0, 0)
  image_widget.setBorders(Pad(3,3,3,3))
  image_widget.setDimensions(100,100)
  inner_frame.addWidget(image_widget)


  # Testing ImageButton
  img_default = gui.loadImage("res/truck.png")
  img_pressed = gui.loadImage("res/truck_bnw.png")
  img_button = gui.ImageButton(img_default, img_pressed)
  img_button.setPosition(20, 200)
  img_button.setDimensions(30,30)
  the_gui.addWidget(img_button)
  
  # Testing elements alignment:

  frame = gui.Frame()
  frame.setDimensions(200,200)
  frame.setLayout(gui.GridLayout(2,6))
  frame.setPosition(0,300)
  the_gui.addWidget(frame)

  

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

if __name__ == "__main__":
  main()