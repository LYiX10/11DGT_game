#24-06-25
#TODO: 
import pygame

pygame.init()

screen = (1600,1200)
screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DGT pixel game")

#variable assignment
jumping = False
sprite_y=650
sprite_x=100
jumpcount = 20
neg = 1
y_velocity = jumpcount
background_x = 0
spring = False
sprite_up = False

game_one_start = False
#img.upload
background_img= pygame.image.load("/Users/lyix/Library/CloudStorage/OneDrive-Personal/Documents/everything/work/school/KWS/2025/11DGT/term_2/game development/version control/V1/round.png").convert_alpha()
sprite = pygame.image.load('/Users/lyix/Library/CloudStorage/OneDrive-Personal/Documents/everything/work/school/KWS/2025/11DGT/term_2/game development/version control/V1/5.png').convert_alpha()
spike = pygame.image.load('/Users/lyix/Library/CloudStorage/OneDrive-Personal/Documents/everything/work/school/KWS/2025/11DGT/term_2/game development/version control/V1/path.png').convert_alpha()
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

    if key[pygame.K_UP]:
        spring = True                    

    if key[pygame.K_RIGHT]:
        background_x -= 30
    
    if spring:
        sprite

    if jumping == True and background_x ==0:
        game_one_start = True

    if game_one_start:
        if background_x > -6300:
            background_x -= 20
        else: #background_x == -5000:
            background_x =0

    screen.blit(background_img,(background_x,0))
    screen.blit(spike,(background_x,0))
    screen.blit(sprite,(sprite_x,sprite_y))
        
    pygame.display.update()

pygame.quit()
