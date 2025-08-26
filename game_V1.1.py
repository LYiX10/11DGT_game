#buggy code 
#jumping code
import pygame

pygame.init()

screen = (1600,1200)
screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DGT pixel game")

#variable making
jumping = False

sprite_y=1000
jumpcount = 20
neg = 0.7
y_velocity = jumpcount



run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key = pygame.key.get_pressed()
    #if statements for keys go here:

        

    if key[pygame.K_SPACE]:
        jumping = True
    
    if jumping:
        sprite_y -= y_velocity
        y_velocity-= neg
        if y_velocity < -jumpcount:                        
            jumping = False
            y_velocity=jumpcount
            


    # if jumping == True:
    #     if jumpcount>= -10:
    #         neg = 1
    #         if jumpcount <0:
    #             neg= -1
    #         sprite_y -= (jumpcount**2)*0.5*neg
    #         jumpcount -= -1
    #     else:
    #         jumping=False
    #         jumpcount=10
        # sprite_y -= jumpcount
        # jumpcount -= 10
        # if jumpcount< 0:
        #     jumping =False


        # if jumpcount>= -10:
        #     neg = 1
        #     if jumpcount <0:
        #         sprite_y -= (jumpcount**2) * 0.5*neg 
        #         jumpcount +=1
        #     else:
        #         jumping = False
        #         jumpcount=100

        # def update(self):
        #     # Add logic for sprite movement, animation, etc.
        #     pass

    screen.fill((70,0,0))


    #sprite allocation goes here:
    pygame.draw.rect(screen, (100,100,100),(50,sprite_y,50,50))

    
    # image = pygame.image.load('V1/comp.png')

    pygame.display.update()

pygame.quit()
