import pygame, colors, sys
from pygame.locals import *

pygame.init()


color = colors.colors()

width = 500
height = 700

screen = pygame.display.set_mode((width, height))
font = pygame.font.Font("Xerox Sans Serif Narrow Bold Oblique.ttf", 50)

class Button():
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        self.surf = surf
        self.butt_area = button_area
        self.butt_color = button_color
        self.text = font.render(text, True, text_color)
        self.text_color = text_color
        self.text_position = ()
        self.butt_position = button_position
        self.button = None
        self.mouse_color = mouse_color Can be set to 'None' if color change due to mouse position is not desired
        self.cursor_pos = (pygame.mouse.get_pos())
        
    def make(self):
        self.button.blit(self.text, self.text_position)
        self.surf.blit(self.button, self.butt_position)
        


class RectButton(Button):
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
        
    
    def draw(self):
        self.button = pygame.Surface(self.butt_area)
        if self.butt_position[0] <= self.cursor_pos[0] <= self.butt_position[0]+self.butt_area[0] and self.butt_position[1] <= self.cursor_pos[1] <= self.butt_position[1]+self.butt_area[1] and self.mouse_color != None:
            self.button.fill(self.mouse_color)
        else:
            self.button.fill(self.butt_color)
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)        
        
    
class CircButton(Button):
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
        
    
    def draw(self):
        circ = pygame.Surface((self.butt_area, self.butt_area))  
        if self.butt_position[0] <= self.cursor_pos[0] <= self.butt_position[0]+self.butt_area and self.butt_position[1] <= self.cursor_pos[1] <= self.butt_position[1]+self.butt_area and self.mouse_color != None:
            circle = pygame.draw.circle(circ, self.mouse_color, (self.butt_area/2, self.butt_area/2), self.butt_area/2)
        else:
            circle = pygame.draw.circle(circ, self.butt_color, (self.butt_area/2, self.butt_area/2), self.butt_area/2) 
        self.button = circ.convert()
        self.button.set_colorkey((0,0,0))         
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)
    
       
class EllipButton(Button):
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
    
    def draw (self):
        elli = pygame.Surface(self.butt_area)
        if self.butt_position[0] <= self.cursor_pos[0] <= self.butt_position[0]+self.butt_area[0] and self.butt_position[1] <= self.cursor_pos[1] <= self.butt_position[1]+self.butt_area[1] and self.mouse_color != None:
            ellipse = pygame.draw.ellipse(elli, self.mouse_color, (0, 0, self.butt_area[0], self.butt_area[1]))
        else:
            ellipse = pygame.draw.ellipse(elli, self.butt_color, (0, 0, self.butt_area[0], self.butt_area[1]))
        self.button = elli.convert()
        self.button.set_colorkey((0, 0, 0))   
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)
    

def display_text(text, color, surf, position, font = pygame.font.Font(None, 30)):
        txt_to_disp = font.render(text, True, color)
        position = (surf.get_width()/2 - txt_to_disp.get_width()/2, surf.get_height()/2 - txt_to_disp.get_height()/2)
        surf.blit(txt_to_disp, position)

#button = EllipButton(screen, (150, 100), color["PINK"], color["RED"], (200, 500), "Play", color["YELLOW"], font)
button = CircButton(screen, (100), color["YELLOW"], color["GOLD"], (200, 500), "Play", color["RED"], font)
#button = RectButton(screen, (150, 100), color["GOLD"], color["YELLOW"], (200, 500), "Play", color["SEA GREEN"], font)


done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        done = True
                        sys.exit()               
                        
        screen.fill(color["BLUE"])
        
        display_text("Welcome", color["RED"], screen, (), font)
        
        
        button.draw()
        button.make()
        button.cursor_pos = pygame.mouse.get_pos()
        
        pygame.display.flip()
        pygame.display.update()