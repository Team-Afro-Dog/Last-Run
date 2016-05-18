'''
Where most of the action is.
User will now be playing the game.
'''

import pygame
import sys
sys.path.insert(0,"Modules")
import background


def game(stats):
   '''Get the level of the game, user's name...etc'''
   playerName = stats["name"]
   difficulty = stats["level"]
   screen = pygame.display.set_mode((800, 800))
   backScreen = background.Background("sampleCode/str1.jpg", screen)
   done = False
   clock = pygame.time.Clock()
   backScreen.display()   

   while not done:

      clock.tick(60) # at most 60FPS
   
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               backScreen.changeToSpeed(10)
            if event.key == pygame.K_LEFT:
               backScreen.changeToSpeed(-10)
         else:
            backScreen.changeToSpeed(0)

      backScreen.move()
      backScreen.display() 
      pygame.display.update()
      






