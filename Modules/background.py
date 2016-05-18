'''
Example on how to use (semi-pseudocode):

   screen = pygame.display.set_mode(100,100)
   Background background("backgroundImg.png", screen, 5)

   while True:

      if makeBackgroundFaster:
         background.changeToSpeed(10) 

      if makeBackgroundBackwards:
         background.changeToSpeed(-5)

      background.move() # move background   
      background.display()   

Works well when going left to right
but buggy when going right to left
'''

import pygame
pygame.display.init()

class Background(object):
   
   def __init__(self, imgPath, screen, speed = 0):
      self.img = pygame.image.load(imgPath)
      self.screen = screen
      self.firstImgXCoordinate = 0
      self.secondImgXCoordinate = self.img.get_width()
      self.speed = speed

   # maybe implement exceptions if cannot find path
   def changeImg(self, imgPath):
      self.img = pygame.image.load(imgPath)

   def changeToSpeed(self, speed):
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



