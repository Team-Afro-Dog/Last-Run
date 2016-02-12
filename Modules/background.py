'''
Version 1.0 
Naive way: have 2 imgs next to each other and move
When first/second image finishes loops it back 

Need to implement:
-Better blit optmization - not blit all of the img background
-Ability to change the screen to another screen
-Move left and right
-Maybe use SpriteSheet class
'''

import pygame

pygame.display.init()

class Background(object):
   
   def __init__(self, imgPath, screen, speed):
      self.img = pygame.image.load(imgPath)
      self.screen = screen
      self.firstImgXCoordinate = 0
      self.secondImgXCoordinate = self.img.get_width()
      self.speed = speed

   def changeSpeed(self, speed):
      self.speed = speed

   def isFirstImgFinish(self):
      return self.firstImgXCoordinate < -1*self.img.get_width() 

   def isSecondImgFinish(self):
      return self.secondImgXCoordinate < -1*self.img.get_width() 

   def move(self):
      if self.isFirstImgFinish():
         self.firstImgXCoordinate = self.screen.get_width()
         
      if self.isSecondImgFinish():
         self.secondImgXCoordinate = self.screen.get_width()

      self.firstImgXCoordinate -= self.speed
      self.secondImgXCoordinate -= self.speed

   def display(self):
      '''
      Need to implement a method to blit only parts of the
      img that will actually display. Right now we are blitting the
      entire thing which slows performance.
      '''
      self.screen.blit(self.img, (self.firstImgXCoordinate,0))   
      self.screen.blit(self.img, (self.secondImgXCoordinate, 0))   
         
      

      
