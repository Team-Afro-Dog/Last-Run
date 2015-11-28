'''Shivam Swarnkar
Test keys: Forward arrow, back word arrow key, space and x.
Work with multiple keys at the same time.
'''
import random, pygame

###########NOT GAME CONTROL ########FOR SNOW#######
# Create an empty array
snow_list = []
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
        sn_x = random.randrange(0, 1000)
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
text = font.render("TEAM AFRO DOG", True, WHITE)


screen = pygame.display.set_mode(size)

 

fill = WHITE
count = 0
x =250
y = 200
x_inc =0
y_inc =0
image_count =0
image =pygame.image.load("walk1_"+str(image_count)+".png")
afro = pygame.image.load("afro.jpg")
clock = 0
pygame.display.set_caption("Control (x axis)")
done = False

snow_ball = False
ball_x = 0
ball_y = 0
ball_x_inc = 0
jump = False
right = False

#########
image1 =pygame.image.load("str1.jpg")
image2 =pygame.image.load("str1.jpg")
x_back1 = 0
y_back1 = 0
x_back2 = 912
y_back2 = 0
x_back1_inc = 0
#######


while not done:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            right = False
                            x_inc = -3
                            x_back1_inc = 0
                            
                        #x_inc is change in cordinate            
                        elif event.key == pygame.K_RIGHT:
                            right = True
                            x_inc = 1
                            x_back1_inc = -5
                            image =pygame.image.load("walk1_"+str(image_count)+".png")

                            image_count += 1
                            if image_count > 3:
                                    image_count =0

                        elif event.key == pygame.K_SPACE and not jump:
                            y_inc = -5
                            image =pygame.image.load("walk1_"+str(image_count)+".png")
                            image_count += 1
                            jump = True
                            if image_count > 3:
                                    image_count =0
                        elif event.key == pygame.K_x:
                            ball_x_inc = 7
                            if not right:
                                    ball_x_inc = -7
                            snow_ball = True
                            ball_x = int(x+30)
                            ball_y = int(y+65)
                            if not right:
                                    image =pygame.image.load("shoot2_"+str(image_count)+".png")
                            else:
                                    image =pygame.transform.flip(pygame.image.load("shoot2_"+str(image_count)+".png"), True, False)
                            image_count += 1
                            if image_count > 4:
                                    image_count =0
                        

                

                elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                        if event.key == pygame.K_LEFT:
                            image_count =0
                            x_inc = 0
                        elif event.key == pygame.K_RIGHT:
                            image_count =0
                            x_inc =0
                            x_back1_inc = 0
                        elif event.key == pygame.K_x:
                            snow_ball = False
                            if not right:
                                    image =pygame.image.load("walk1_"+str(image_count)+".png")
                            else:
                                    image =pygame.transform.flip(pygame.image.load("walk1_"+str(image_count)+".png"), True, False)
                       
        if y + y_inc <= 100:
                y_inc *= -1
        if y + y_inc == 200:
                y += y_inc
                y_inc =0
                jump = False
        if not snow_ball:
                image =pygame.image.load("walk1_"+str(image_count)+".png")
        #making change of images slower(change the clock += num to see the affect)
        if x_inc != 0:
                clock +=1
                if clock %5 == 0:
                        image_count += 1
                        if image_count >3:
                                image_count =1
  
        #making sure that avatar doesn't cross the frame                
        if x +x_inc < size[0]-37 and y + y_inc <= size[1]-37 \
           and x + x_inc > -15 and y >-15:
                x += x_inc
                y += y_inc
        ball_x += ball_x_inc

        

        screen.fill(fill)
        if right and not snow_ball:
                image = pygame.transform.flip(image,True, False)
        ###############################################
        x_back1 += x_back1_inc
        x_back2 += x_back1_inc

        if (x_back1==-910):
                x_back1 =912
        elif (x_back1==2):
                x_back1 =0
        if (x_back2==2):
                x_back2 =0
        if (x_back2==-910):
                x_back2 =912
        ###############################################
        screen.blit(image1, (x_back1,y_back1))
        screen.blit(image2, (x_back2, y_back2))
        screen.blit(image, (x, y))
        pygame.draw.rect(screen, BLACK, [0,284,920,300]) #platform
        if snow_ball or (ball_x != 0 and ball_y !=0):
                pygame.draw.circle(screen, RED, [ball_x, ball_y],5)
                if( ball_x > 910):
                        ball_x = 0
                        ball_y = 0
                        snow_ball = False
                                   
        #########################SNOW (NOT IMPORTANT FOR CONTROL##################################
        # Process each snow flake in the list
        for i in range(len(snow_list)):
                # Draw the snow flake
                pygame.draw.circle(screen, WHITE, snow_list[i], 2)
##                pygame.draw.circle(screen, RED, [snow_list[i][0]+25,snow_list[i][1]], 2)
##                pygame.draw.circle(screen, WHITE, [snow_list[i][0]+35,snow_list[i][1]], 2)
##                pygame.draw.circle(screen, YELLOW, [snow_list[i][0]+45,snow_list[i][1]], 2)
##                # Move the snow flake down one pixel
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
                screen.blit(afro, [450, 150])

        pygame.display.flip()
        

pygame.quit()





