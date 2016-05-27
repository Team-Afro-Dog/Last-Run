import pygame, colors, sys
from pygame.locals import *

pygame.init()


color = colors.colors()

width = 500
height = 700

screen = pygame.display.set_mode((width, height))
font = pygame.font.Font("Xerox Sans Serif Narrow Bold Oblique.ttf", 50)

class Button():
    def __init__(self, surf, button_area, button_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        self.surf = surf
        self.butt_area = button_area
        self.butt_color = button_color
        self.text = font.render(text, True, text_color)
        self.text_color = text_color
        self.text_position = ()
        self.butt_position = button_position
        self.button = None
        
        def lighten_color(color):
                lst = [color[0], color[1], color[2]]
                if color[0] <= 245:
                        lst[0] = color[0]+10
                if color[1] <= 245:
                        lst[1] = color[1]+10
                if color[2] <= 245:
                        lst[2] = color[2]+10        
                return (lst[0], lst[1], lst[2])        
        self.light_butt_color = lighten_color(button_color)
        
    def make_button(self):
        self.surf.blit(self.button, (0,0))
        self.button.blit(self.text, (0,0))

    
'''       rect = pygame.Surface(shape_area)
                        rect.fill(shape_color)
                        display_text(text, text_color, rect, "rect", ())
                        surf.blit(rect, position)    '''
class RectButton(Button):
    def __init__(self, surf, button_area, button_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
        self.button = pygame.Surface(self.butt_area)
        self.button.fill(self.butt_color)
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)
        
    
class CircButton(Button):
    def __init__(self, surf, button_area, button_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
        circ = pygame.Surface((self.butt_area, self.butt_area)) 
        circle = pygame.draw.circle(circ, self.butt_color, self.butt_position, self.butt_area)
        self.button = circ.convert()
        self.button.set_colorkey((255,0,0))
        
        '''circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(8,8),8)
circle = circ_sur.convert()'''
    
#class EllipButton(Button)
    

def display_text(text, color, surf, position, font = pygame.font.Font(None, 30)):
        txt_to_disp = font.render(text, True, color)
        
        
        #if surf_type == "rect" and position == ():
        position = (surf.get_width()/2 - txt_to_disp.get_width()/2, surf.get_height()/2 - txt_to_disp.get_height()/2)
        '''elif surf_type == "circle":
                position = (position[0]-txt_to_disp.get_width()/2, position[1]-txt_to_disp.get_height()/2)
        elif surf_type == "ellipse":
                position = ((position[1][0]/2-txt_to_disp.get_width()/2)+position[0][0], (position[1][1]/2-txt_to_disp.get_height()/2)+position[0][1])'''
        surf.blit(txt_to_disp, position)

button = CircButton(screen, (50), color["RED"], (200, 500), "Play", color["YELLOW"], font)

done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        done = True
                        sys.exit()               
                        
        
        screen.fill(color["LAVENDER"])
        
        display_text("Welcome", color["BLUE"], screen, (), font)
        
        
        button.make_button()
        
        pygame.display.flip()