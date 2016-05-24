'''
Create Text on Screen

'''

def display_text(text, color, surf, surf_type, position, font = pygame.font.Font(None, 30)):
        #Display string, text, on a surface, surf, at position, position with standard font or font of ur choosing
        #If position is an empty tuple, (), the text is displayed at the center of the surface
        
        txt_to_disp = font.render(text, True, color)
        
        
        if surf_type == "rect" and position == ():
        #display text on any rectangular surface like the screen
                position = (surf.get_width()/2 - txt_to_disp.get_width()/2, surf.get_height()/2 - txt_to_disp.get_height()/2)
        elif surf_type == "circle":
        #display text on any circular surface
                position = (position[0]-txt_to_disp.get_width()/2, position[1]-txt_to_disp.get_height()/2)
        elif surf_type == "ellipse":
        #display text on any elliptical surface
                position = ((position[1][0]/2-txt_to_disp.get_width()/2)+position[0][0], (position[1][1]/2-txt_to_disp.get_height()/2)+position[0][1])
        surf.blit(txt_to_disp, position)
        
        
def make_button(shape, shape_area, shape_color, text, text_color, surf, position, font = pygame.font.Font(None, 30)):
        #Create a button of shape, shape, with area, shape_area, of color, shape_color, with a text, text of color, text_color, on the button, on a surface, surf, usually a screen, at position, position on the screen, with an optional font of ur choosing
        if shape == "rect":
        #rectangular button
                rect = pygame.Surface(shape_area)
                rect.fill(shape_color)
                display_text(text, text_color, rect, "rect", ())
                surf.blit(rect, position)
        if shape == "circle":
        #circular button
                circle = pygame.draw.circle(surf, shape_color, position, shape_area)
                display_text(text, text_color, surf, "circle", position)
        if shape == "ellipse":
        #elliptical button
                ellipse = pygame.draw.ellipse(surf, shape_color, (position[0], position[1], shape_area[0], shape_area[1]))
                display_text(text, text_color, surf, "ellipse", (position, shape_area))