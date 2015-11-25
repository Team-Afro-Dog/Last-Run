'''Shivam Swarnkar'''
import random, pygame

###########NOT GAME CONTROL ########FOR SNOW#######
# Create an empty array
snow_list = []
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
        sn_x = random.randrange(0, 920)
        sn_y = random.randrange(0, 540)
        snow_list.append([sn_x, sn_y])

##########END SNOW#################################


pygame.init()

size = [920,540]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
font = pygame.font.Font(None, 36)
text = font.render("TEAM AFRO DOG", True, BLACK)


screen = pygame.display.set_mode(size)

 

fill = WHITE
count = 0
x =250
y = 250
x_inc =0
y_inc =0
image_count =1
image =pygame.image.load(str(image_count)+".png")
clock = 0
pygame.display.set_caption("Control (x axis)")
done = False
while not done:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_inc = -0.3
                            
                        #x_inc is change in cordinate            
                        elif event.key == pygame.K_RIGHT:
                            x_inc = 0.3
                            image =pygame.image.load(str(image_count)+".png")
                            image_count += 1
                            if image_count > 4:
                                    image_count =1

                elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                        if event.key == pygame.K_LEFT:
                            x_inc = 0
                        elif event.key == pygame.K_RIGHT:
                            x_inc =0

        image =pygame.image.load(str(image_count)+".png")
        #making change of images slower(change the clock += num to see the affect)
        if x_inc != 0:
                clock +=1
                if clock %100 == 0:
                        image_count += 1
                        if image_count >4:
                                image_count =1
        #making sure that avatar doesn't cross the frame                
        if x +x_inc < size[0]-37 and y + y_inc <= size[1]-37 \
           and x + x_inc > -15 and y >-15:
                x += x_inc
                y += y_inc

        

        screen.fill(fill)
        screen.blit(image, (x, y))
        screen.blit(text, [350, 200])
        pygame.draw.rect(screen, BLACK, [0,295,920,300]) #platform
        #########################SNOW (NOT IMPORTANT FOR CONTROL##################################
        # Process each snow flake in the list
        for i in range(len(snow_list)):
                # Draw the snow flake
                pygame.draw.circle(screen, BLUE, snow_list[i], 2)
                pygame.draw.circle(screen, RED, [snow_list[i][0]+25,snow_list[i][1]], 2)
                pygame.draw.circle(screen, GREEN, [snow_list[i][0]+35,snow_list[i][1]], 2)
                pygame.draw.circle(screen, YELLOW, [snow_list[i][0]+45,snow_list[i][1]], 2)
                # Move the snow flake down one pixel
                snow_list[i][1] += 1
                # If the snow flake has moved off the bottom of the screen
                if snow_list[i][1] > 400:
                        # Reset it just above the top
                        sn_y = random.randrange(-50, -10)
                        snow_list[i][1] = sn_y
                        # Give it a new x position
                        sn_x = random.randrange(0, 920)
                        snow_list[i][0] = sn_x
        #####################################END SNOW###########################################
        pygame.display.flip()
        

pygame.quit()





