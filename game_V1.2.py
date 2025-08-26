#imported sprites and background templates
import pygame

pygame.init()

screen = (1600,1200)
screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DGT pixel game")

#variable 
jumping = False
sprite_y=1000
jumpcount = 20
neg = 0.7
y_velocity = jumpcount

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
    if key[pygame.K_s]:
        sprite_y = -1000
        
    if key[pygame.K_SPACE]:
        jumping = True
    
    if jumping:
        sprite_y -= y_velocity
        y_velocity-= neg
        if y_velocity < -jumpcount:                        
            jumping = False
            y_velocity=jumpcount



    screen.blit(background_img, (0, 0))
    screen.blit(sprite,(100,sprite_y))
        
    pygame.display.update()

pygame.quit()
