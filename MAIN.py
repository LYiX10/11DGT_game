#22/06/25
#TODO: create a jump function, create boarder collisons. 
import pygame

pygame.init()

screen = (1920,1080)
screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DUMMY GAME")
#set the coordinate of where the spirte will appear and it height and width
sprite_x=0
sprite_y=50
#width and height of the sprite
sprite_width = 20
sprite_height = 30
#set verlocity to control speed of sprite
velocity = 20

#jump code
jumping = False #checks whether the sprite has actually jumped
jump_count = 10 #counter to track how many pixels the character going to 'jump'

#movemENT Code
#moves character for as long as the key gets held donw in whatever direcetion
#set up lists to do this


#DRAW THE RECTANGLE WHICH WILL REPRESENT THE CHARACT IN GAME

run = True
while run:
    pygame.time.delay(60) #setting the clock speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT] and sprite_x >velocity-5:
    #     sprite_x -= velocity 

    # if keys[pygame.K_RIGHT] and sprite_x< screen_width - sprite_width-velocity+5:
    #     sprite_x+=velocity

    # if keys[pygame.K_UP] and sprite_y < screen_height-screen_width-velocity-5:
    #     sprite_y -=velocity
    # if keys[pygame.K_DOWN] and sprite_y>screen_height-screen_width-velocity+5:
    #     sprite_y+=velocity


    if keys[pygame.K_RIGHT] and sprite_x > screen_width:
        sprite_x = screen_width

    if keys[pygame.K_LEFT] and sprite_x < 6:
        sprite_x = 0
    
    if keys[pygame.K_UP] and sprite_y < 0:
        sprite_y = 0

    # if keys[pygame.K_DOWN] and sprite_y < screen_height:
    #     sprite_y = screen_height




    if keys[pygame.K_LEFT]: #capitcal K stands for KEY 
        sprite_x -= velocity
    if keys[pygame.K_RIGHT]:
        sprite_x += velocity 
    if keys[pygame.K_UP]: 
        sprite_y -= velocity 
    if keys[pygame.K_DOWN]: 
        sprite_y += velocity
    if keys[pygame.K_ESCAPE]:
        run = False
    screen.fill((0,0,0)) #setting the background color as black (RGB)
    #update the screen, otherwise nothing will draw
    pygame.draw.rect(screen,(225,0,225), (sprite_x,sprite_y,sprite_width,sprite_height))

    pygame.display.update()

pygame.quit()