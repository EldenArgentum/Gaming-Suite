import pygame
from sys import exit
import os

Directory = "/Users/mootahir/Desktop/Programming/GitKraken Stuff/Gaming Suite"
def DirectorySet(Dir):
    os.chdir(Dir)
    
DirectorySet(Directory) # IF YOU ARE USING THIS PROGRAM, DELETE THIS LINE, I WAS JUST HAVING ISSUES WITH MY DIRECTORY.

pygame.init()
screen = pygame.display.set_mode((800, 400)) # Parameter is a tuple with (width, height)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
runner_font = pygame.font.Font('Font/Pixeltype.ttf', 50)

# TEST SURFACE FOR DEMONSTRATION... BETTER AND PRETTIER TO USE PNG'S, AND CONVERT IT
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

# GROUND AND SKY AND TEXT -- STATIC STUFF
# GROUND
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
# TEXT
text_surface = runner_font.render("Runner", False, (64, 64, 64))
text_rectangle = text_surface.get_rect(center = (400, 100))

# SNAIL SURFACE/RECTANGLE STUFF
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (900, 300))
# snail_surface_2 = pygame.image.load('graphics/snail/snail2.png')

# PLAYER SURFACE/RECTANGLE STUFF
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

player_gravity = 0

while True:     # Entire game will run in this loop; until game is done, the program will stay open
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        # #     print("mouse down")
        
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print("Collided wtih player")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")
        
        if event.type == pygame.KEYUP:
            print("Key up")
        
        
    # PLACING STATIC BLOCKS
    screen.blit(sky_surface, (00, 00))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle)
    pygame.draw.rect(screen, "#c0e8ec", text_rectangle, 10)
    # pygame.draw.line(screen, "Black", (0, 0), pygame.mouse.get_pos())
    pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))
    screen.blit(text_surface, text_rectangle)
    # snail_x_pos -= 4
    # screen.blit(snail_surface_1, (snail_x_pos, 250))
    
    # SNAIL AND SNAIL MOVEMENT
    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.x -= 4
    if snail_rectangle.right < -100:
        snail_rectangle.left = 800
    
    # PLAYER SETTING
    screen.blit(player_surface, player_rectangle)
    
    player_gravity += 1
    player_rectangle.y += player_gravity
    
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Jump!")
    
    # if player_rectangle.colliderect(snail_rectangle):
    #     snail_rectangle.bottom = 80
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
        
    
    # draw all of the elements
    # update everything
    pygame.display.update()
    clock.tick(60)