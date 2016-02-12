import spritesheet
import ssAccessor
import pygame
import background

def main():
   screen = pygame.display.set_mode((900,350))
   bg = background.Background("str1.jpg", screen, 10) 
   ss = spritesheet.SpriteSheet("walkSprite.png", (104,150), (624,450))
   ac1 = ssAccessor.SSAccessor(ss, (0,13), 0)
   ac2 = ssAccessor.SSAccessor(ss, (0,13), 0)
   for i in range(0, 500):   
      bg.display()
      ac1.display(screen, (250, 70))
      ac2.display(screen, (503,100))
      pygame.display.update()
      pygame.time.delay(50)
      #screen.blit(background, (0,0))
      bg.move()
main()
