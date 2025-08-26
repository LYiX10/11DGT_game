#inserted the background template
#background can move when left and right keys are pressed
import pygame

pygame.init()

screen = (1600,1200)
screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DGT pixel game")

#variable assignment
jumping = False
sprite_y=1000
sprite_x=100
jumpcount = 20
neg = 1
y_velocity = jumpcount
background_x = 0

#img.upload
background_img= pygame.image.load('/Users/lyix/Library/CloudStorage/OneDrive-Personal/Documents/everything/work/school/KWS/2025/11DGT/term2/game development/version control/V1/img_V1/round.png').convert_alpha()
sprite = pygame.image.load('/Users/lyix/Library/CloudStorage/OneDrive-Personal/Documents/everything/work/school/KWS/2025/11DGT/term2/game development/version control/V1/img_V1/5.png').convert_alpha()

run = True
while run:
    pygame.time.delay(10)
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

    if key[pygame.K_RIGHT]:
        background_x -= 30


    if key[pygame.K_LEFT]:
        background_x += 30


    screen.blit(background_img,(background_x,0))
    screen.blit(sprite,(sprite_x,sprite_y))
        
    pygame.display.update()

pygame.quit()
