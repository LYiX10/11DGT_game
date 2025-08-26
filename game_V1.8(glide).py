#attempt to try make the glide function toperform one glide action to one barrier at a time
#get rid of jump code. 

import pygame
import os

path=os.getcwd()
full_path=path+"/img_V1"

pygame.init()

screen = (1600,1200)
screen_width = 1600
screen_height = 1200

screen = pygame.display.set_mode((screen))
pygame.display.set_caption("DGT pixel game")

#variable assignment
glide = False
glide_up = True
glide_down = False
sprite_y=650 #120
sprite_x=100
jumpcount = 20
jumpcount_glide = 32
neg = 1
y_velocity = jumpcount
y_velocity_glide = jumpcount_glide
background_x = 0

game_one_start = False
#img.upload
background_img= pygame.image.load(full_path +"/round.png").convert_alpha()
sprite = pygame.image.load(full_path+"/5.png").convert_alpha()
spike = pygame.image.load(full_path+'/path.png').convert_alpha()
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    
    key = pygame.key.get_pressed()
    #if statements for keys go here:
        
    if key[pygame.K_SPACE]:
        game_one_start = True

    if key[pygame.K_UP]:
        glide = True

    if glide and glide_up:
        sprite_y -= y_velocity_glide
        # y_velocity_glide-= neg
        if sprite_y < 120:                        
            sprite_y = 120
            glide = False      
            glide_up = False     
            glide_down = True
            y_velocity_glide=jumpcount_glide
    if glide and glide_down: 
            sprite_y += y_velocity_glide
            if sprite_y > 650: 
                sprite_y = 650
                glide = False
                glide_down = False
                glide_up = True
                y_velocity_glide=jumpcount_glide




    if game_one_start == True: #and background_x ==0:
        if background_x > -6300:
            background_x -= 20
        else: 
            background_x =0

    screen.blit(background_img,(background_x,0))
    screen.blit(spike,(background_x,0))
    screen.blit(sprite,(sprite_x,sprite_y))
        
    pygame.display.update()

pygame.quit()
