import pygame, colors, sys#, button_class
from pygame.locals import *

pygame.init()
        

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
        self.clicked = False
    
    def draw(self):
        print "hmmm, maybe I should draw  something"
        
    def make(self):
        self.button.blit(self.text, self.text_position)
        self.surf.blit(self.button, self.butt_position)  
        
    def display(self):
        self.draw()
        self.make()
        self.cursor_pos = pygame.mouse.get_pos()    
        


class RectButton(Button):
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
        
    
    def draw(self):
        self.button = pygame.Surface(self.butt_area)
        
        if self.butt_position[0] <= self.cursor_pos[0] <= self.butt_position[0]+self.butt_area[0] and self.butt_position[1] <= self.cursor_pos[1] <= self.butt_position[1]+self.butt_area[1] and self.mouse_color != None:
            self.button.fill(self.mouse_color)
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            
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
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True            
            
        else:
            circle = pygame.draw.circle(circ, self.butt_color, (self.butt_area/2, self.butt_area/2), self.butt_area/2) 
            
        self.button = circ.convert()
        self.button.set_colorkey((0,0,0))         
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)
        self.make()
    
       
class EllipButton(Button):
    def __init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30)):
        Button.__init__(self, surf, button_area, button_color, mouse_color, button_position, text, text_color, font = pygame.font.Font(None, 30))
    
    def draw (self):
        elli = pygame.Surface(self.butt_area)
        
        if self.butt_position[0] <= self.cursor_pos[0] <= self.butt_position[0]+self.butt_area[0] and self.butt_position[1] <= self.cursor_pos[1] <= self.butt_position[1]+self.butt_area[1] and self.mouse_color != None:
            ellipse = pygame.draw.ellipse(elli, self.mouse_color, (0, 0, self.butt_area[0], self.butt_area[1]))
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True            
            
        else:
            ellipse = pygame.draw.ellipse(elli, self.butt_color, (0, 0, self.butt_area[0], self.butt_area[1]))
            
        self.button = elli.convert()
        self.button.set_colorkey((0, 0, 0))   
        self.text_position = (self.button.get_width()/2 - self.text.get_width()/2, self.button.get_height()/2 - self.text.get_height()/2)
        self.make()
        
class Background():
    def __init__(self):
        self
    

def display_text(text, color, surf, surf_type, position, font = pygame.font.Font(None, 30)):
        #Display string, text, on a surface, surf, at position, position with standard font or font of ur choosing
        #If position is an empty tuple, (), the text is displayed at the center of the surface
        txt_to_disp = font.render(text, True, color)
        
        
        if surf_type == "rect" and position == ():
        #display text on any rectangular surface like the screen
        #This is most used
                position = (surf.get_width()/2 - txt_to_disp.get_width()/2, surf.get_height()/2 - txt_to_disp.get_height()/2)
        elif surf_type == "circle":
        #display text on any circular surface
                position = (position[0]-txt_to_disp.get_width()/2, position[1]-txt_to_disp.get_height()/2)
        elif surf_type == "ellipse":
        #display text on any elliptical surface
                position = ((position[1][0]/2-txt_to_disp.get_width()/2)+position[0][0], (position[1][1]/2-txt_to_disp.get_height()/2)+position[0][1])
        surf.blit(txt_to_disp, position)
        


def page(page_type, text_color, screen, text_pos, text_font = pygame.font.Font(None, 30)):
    if page_type == "Name Page":
        display_text("Name", text_color, screen, "rect", text_pos, text_font)
    elif page_type == "Welcome Page":
        display_text("Last Run", text_color, screen, "rect", text_pos, text_font)
    elif page_type == "Game Page":
        display_text("Game Screen", text_color, screen, "rect", text_pos, text_font)
    elif page_type == "End Page":
        display_text("End", text_color, screen, "rect", text_pos, text_font)
    elif page_type == "Mode Page":
        display_text("Difficulty Mode", text_color, screen, "rect", text_pos, text_font)

def pauseMenu(screen):
    pause_surf = pygame.Surface((250, 210))
    pause_surf.fill(color["PURPLE"])
    main_menu = RectButton(screen, (250, 70), color["RED"], color["DEEP PINK"], (125,250), "Main Menu", color["LAWN GREEN"])
    resume = RectButton(screen, (250, 70), color["RED"], color["DEEP PINK"], (125,320), "Resume", color["LAWN GREEN"])
    quit = RectButton(screen, (250, 70), color["RED"], color["DEEP PINK"], (125,390), "Quit", color["LAWN GREEN"])
    
    screen.blit(pause_surf, (125, 250))
    
    main_menu.display()
    resume.display()
    quit.display() 
    
    if main_menu.clicked:
        return "main_menu"
    if resume.clicked:
        return "resume"
    if quit.clicked:
        return "quit"

def modeMenu(screen):
    easy = RectButton(screen, (250, 70), color["SALMON"], color["DEEP PINK"], (1,200), "Easy", color["LAWN GREEN"])
    medium = RectButton(screen, (250, 70), color["DARK SALMON"], color["DEEP PINK"], (1,300), "Medium", color["LAWN GREEN"])
    hard = RectButton(screen, (250, 70), color["FIREBRICK"], color["DEEP PINK"], (1,400), "Hard", color["LAWN GREEN"])    
    
    easy.display()
    medium.display()
    hard.display()
    
    if easy.clicked:
        return "easy"
    if medium.clicked:
        return "medium"
    if hard.clicked:
        return "hard"   


def game_screen(mode, screen):
    if mode == "easy":
        #run the game here in easy mode
        pause_button.clicked = False
        screen.fill(color["YELLOW"])
        page("Game Page", color["BLUE"], screen, (), font)
        display_text("Pssh. This is easy peazy!", color["PURPLE"], screen, "rect", (125, 400))
        pause_button.display() 
        
    elif mode == "medium":
        #run the game here in medium mode
        pause_button.clicked = False
        screen.fill(color["YELLOW"])
        page("Game Page", color["BLUE"], screen, (), font)
        display_text("U sure? Gonna get Hard!", color["PURPLE"], screen, "rect", (125, 400))
        pause_button.display()  
                
    elif mode == "hard":
        #run the game here in hard mode
        pause_button.clicked = False
        screen.fill(color["YELLOW"])
        page("Game Page", color["BLUE"], screen, (), font)
        display_text("Hey Tough Guy, Strap ur Boots cos u r in for a", color["PURPLE"], screen, "rect", (30, 400))
        display_text("HELL'of a RIDE!!!", color["PURPLE"], screen, "rect", (170, 430))
        pause_button.display()
    
        
color = colors.colors()
width = 500
height = 700
screen = pygame.display.set_mode((width, height))
#background = Background(background_image)
font = pygame.font.Font("Xerox Sans Serif Narrow Bold Oblique.ttf", 70)
play_button = CircButton(screen, (100), color["SPRING GREEN"], color["LAWN GREEN"], (30, 550), "Play", color["PURPLE"])
exit_button = EllipButton(screen, (100, 75), color["RED"], color["DEEP PINK"], (333, 560), "Exit", color["LAWN GREEN"])
pause_button = EllipButton(screen, (100, 75), color["RED"], color["DEEP PINK"], (1, 1), "Pause", color["LAWN GREEN"])
back_button = RectButton(screen, (75, 50), color["RED"], color["DEEP PINK"], (424,1), "back", color["LAWN GREEN"])       
mode = ""   
pause_button_pressed = False
back_button_pressed = False
play_button_pressed = False
clock = pygame.time.Clock()
done = False

while not done:
        screen.fill(color["ORANGE"])
        
        page("Welcome Page", color["BLUE"], screen, (), font)
        display_text("What's your name?", color["PURPLE"], screen, "rect", (150, 430))
        
        play_button.display()
        
        exit_button.display()        
        
        if exit_button.clicked:
            done = True
            sys.exit()
        
        
        if play_button.clicked:
            screen.fill(color["YELLOW"])
            page("Mode Page", color["GRAY"], screen, (1,1), font)
            mode = modeMenu(screen)
            back_button.display()
            if back_button.clicked:
                play_button.clicked = False 
                back_button.clicked = False
               
    
        if mode:
            play_button.clicked = False
            game_screen(mode, screen)
                     
            
        if pause_button.clicked:
            pause_button_pressed = True 
            #pause in game activities here
        
        if pause_button_pressed:
            sel = pauseMenu(screen)
            if sel == "main_menu":
                play_button.clicked = False
                pause_button_pressed = False
                mode = ""
                
            elif sel == "resume":
                pause_button_pressed = False
                #resume in game activities here
                
            elif sel == "quit":
                done = True
                sys.exit()                            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                sys.exit()        
        
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()
