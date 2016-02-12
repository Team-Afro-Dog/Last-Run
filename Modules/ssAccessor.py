'''
Version 1.0
Future Implementations:
-Work with uneven frames
-Still debating should the user define when to increment() or 
let display() do the work
'''
import pygame

class SSAccessor(object):
   '''
   Works with SpriteSheet object
   Each SSAccessor can only have 1 spritesheet
   The purpose of this is to minimize the amount of times to 
   load spritesheets. Every spritesheet should only be
   loaded once per game and every object should "share" the spritesheet pointer. 
   This object will request a part of the image needed in the spritesheet. 
   *That means DO NOT modify the spritesheet like you own it!
   '''

   def __init__(self, spritesheet, frameRange, defaultFrame = None):
      '''
      Note: Total of 5 members
      frameRange is a tuple
      '''
      self.spritesheet = spritesheet
      self.minFrame, self.maxFrame = frameRange
      
      if defaultFrame is None:
         self.defaultFrame = self.minFrame
         self.currentFrame = self.minFrame
      else:
         self.defaultFrame = defaultFrame
         self.currentFrame = self.defaultFrame

   def moveToDefaultFrame(self):
      self.currentFrame = self.defaultFrame 

   def increment(self):
      '''Go back to the first frame of the frame range'''
      if self.currentFrame > self.maxFrame:
         self.currentFrame = self.minFrame
      else:
         self.currentFrame += 1

   def display(self, surface, xyOfSurface = (0,0)):
      '''
      Displays current frame and then increments frame by 1.
      You may comment out increment() if you prefer more micromanagement.      
      xyOfSurface takes a tuple
      '''
      self.spritesheet.display(self.currentFrame, surface, xyOfSurface)
      self.increment()



