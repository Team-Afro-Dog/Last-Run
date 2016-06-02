'''
Button Class:
Creates Rectangular, Circular and Elliptical buttons that 
change color when the cursor is on them.

Format for using this class in game:

Outside while loop:
button = RectButton(screen, (100, 75), ...)

In while loop:
button.draw()
button.make()
button.cursor_pos = pygame.mouse.get_pos()
'''

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
        self.mouse_color = mouse_color #Can be set to 'None' if color change due to mouse position is not desired
        self.cursor_pos = (pygame.mouse.get_pos())
        
    def make_button(self):
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