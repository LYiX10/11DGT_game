#added stars into the game. //BUG 
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
sprite_y=650 #120 for upper boundary 
sprite_x=100
jumpcount_glide = 32
neg = 1
y_velocity_glide = jumpcount_glide
background_x = 0
game_one_start = False

#img.upload
background_img= pygame.image.load(full_path +"/round.png").convert_alpha()
sprite = pygame.image.load(full_path+"/5.png").convert_alpha()
boundary = pygame.image.load(full_path+'/boundary.png').convert_alpha()
spike = pygame.image.load(full_path+'/spike.png').convert_alpha()
star = pygame.image.load(full_path+'/star.png').convert_alpha()

spike_mask = pygame.mask.from_surface(spike)
# spike_mask_img = spike_mask.to_surface()
sprite_mask =  pygame.mask.from_surface(sprite)
# sprite_mask_img = sprite_mask.to_surface()


#even controller
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
                


    if game_one_start == True: 
        if background_x > -6300:
            background_x -= 20
        else: 
            background_x =0

    if sprite_mask.overlap(spike_mask,(background_x-sprite_x,-sprite_y)):
        print('collide')
        background_x = 0
        pygame.time.wait(1000)



    screen.blit(background_img,(background_x,0))
    screen.blit(spike,(background_x,0))
    screen.blit(boundary,(background_x,0))
    
    
    
    # screen.blit(spike_mask_img,(background_x,0))
    
    screen.blit(spike,(background_x,0))
    screen.blit(sprite,(sprite_x,sprite_y))
    screen.blit(star,(background_x,-50))
    # screen.blit(sprite_mask_img,(sprite_x,sprite_y))
        
    pygame.display.update()

pygame.quit()
