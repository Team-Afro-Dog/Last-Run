'''
Version 1.0
Can only work with uniform frames
Works with SSAccessor object
'''
import pygame

# before this line is called, make sure you called pygame.display.set_mode()
pygame.display.init() 

class SpriteSheet(object):
   '''Should only load a spritesheet once per game'''
   def __init__(self, imgPath, frameLW, spriteDimensions):
      '''
      Note: Total of 6 members
      frameLW and spriteDimensions are tuples 
      '''
      self.img = pygame.image.load(imgPath)
      self.frameLength, self.frameWidth  = frameLW
      self.spriteLength, self.spriteWidth = spriteDimensions
      self.maxFramesPerRow = self.spriteLength / self.frameLength

   def getCoordinate(self, frameNum):
      '''
      Returns a tuple which tells how many frames it takes to 
      get to the top left corner of frameNum. The first index is 
      how many frames it takes horizontally and the second vertically.
      ''' 
      return ((frameNum % self.maxFramesPerRow),(frameNum / self.maxFramesPerRow))

   def display(self, frame, surface, xySurface):
      '''
      Since we know the number of frames to get to a certain frame,
      we just need to multiply it by the dimension of a standard
      frame to get the exact pixel coordinates.
      Blits a frame sized image starting from xySurface (top-left coordinate)
      '''
      x, y = self.getCoordinate(frame)
      pixelsFromOrigin_x = x * self.frameLength
      pixelsFromOrigin_y = y * self.frameWidth
      surface.blit(self.img, xySurface, (pixelsFromOrigin_x, pixelsFromOrigin_y, self.frameLength, self.frameWidth))
      
