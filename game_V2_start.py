# insert the remade longer background, boundary, and spikes (because is dont want the game to be an infinite loop)
#becuase i changed the position of the boundary and the spikes (i shifted them lower), i had to also change the positon of the player;s y axis to match the background. 
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
sprite_y=738 #210 for upper boundary 
sprite_x=100
jumpcount_glide = 32
neg = 1
y_velocity_glide = jumpcount_glide
background_x = 0
game_one_start = False

#img.upload
background_img= pygame.image.load(full_path +"/background_new.png").convert_alpha()
sprite = pygame.image.load(full_path+"/5.png").convert_alpha()
boundary = pygame.image.load(full_path+'/boundary_new.png').convert_alpha()
spike = pygame.image.load(full_path+'/spike_new.png').convert_alpha()


spike_mask = pygame.mask.from_surface(spike)
# spike_mask_img = spike_mask.to_surface()
sprite_mask =  pygame.mask.from_surface(sprite)
# sprite_mask_img = sprite_mask.to_surface()

start = pygame.image.load(full_path+'/start.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, img,):                      
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False    

    def draw(self):
        pos = pygame.mouse.get_pos()
        print(pos)
        if self.rect.collidepoint(pos):
            print('HOVER')
        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(100, 200, start)

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
        if sprite_y < 210:                        
            sprite_y = 210
            glide = False      
            glide_up = False     
            glide_down = True
            y_velocity_glide=jumpcount_glide
            
    if glide and glide_down: 
            sprite_y += y_velocity_glide
            if sprite_y > 738: 
                sprite_y = 738
                glide = False
                glide_down = False
                glide_up = True
                y_velocity_glide=jumpcount_glide

    if game_one_start == True: 
        if background_x > -25500:
            background_x -= 20
        else: 
            background_x =0
            pygame.time.wait(1000)

    if sprite_mask.overlap(spike_mask,(background_x-sprite_x,-sprite_y)):
        print('collide')
        background_x = 0
        pygame.time.wait(1000)



    screen.blit(background_img,(background_x,0))
    screen.blit(spike,(background_x,0))
    screen.blit(boundary,(background_x,0))
    # screen.blit(start, (100,200))
    start_button.draw()

    
    
    
    # screen.blit(spike_mask_img,(background_x,0))
    
    screen.blit(spike,(background_x,0))
    screen.blit(sprite,(sprite_x,sprite_y))
    # screen.blit(sprite_mask_img,(sprite_x,sprite_y))
        
    pygame.display.update()

pygame.quit()
