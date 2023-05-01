import pygame
from sys import exit
import os
# import inspect

def display_score():
    global score
    # current_time = pygame.time.get_ticks()   Tutorial's way... we're doing this my way!
    # print(current_time)
    score_surface = test_font.render(f"Score: {score}", False, (32, 32, 32))
    score_rectangle = score_surface.get_rect(center = (400, 100))
    screen.blit(score_surface, score_rectangle)
    if snail_rectangle.right == player_rectangle.left:
        score += 1

score = 0

# Directory = "/Users/mootahir/Desktop/Programming/GitKraken Stuff/Gaming Suite/Runner"
# def DirectorySet(Dir):
#     os.chdir(Dir)
    
# DirectorySet(Directory) # IF YOU ARE USING THIS PROGRAM, DELETE THIS LINE, I WAS JUST HAVING ISSUES WITH MY DIRECTORY.

# filename = os.path.abspath("Runner.py") # Will print entire directory
# filename = os.path.basename(__file__) # Will print just the script name
# path = os.path.dirname(os.path.abspath(filename))
path = os.path.dirname(__file__)

# print(path, "---------------")

pygame.init()
screen = pygame.display.set_mode((800, 400)) # Parameter is a tuple with (width, height)
pygame.display.set_caption(f'Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(f'{path}/Font/Pixeltype.ttf', 50)
game_active = True

runner_title = pygame.font.Font(f'{path}/Font/Pixeltype.ttf', 50)


# TEST SURFACE FOR DEMONSTRATION... BETTER AND PRETTIER TO USE PNG'S, AND CONVERT IT
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')

# GROUND AND SKY AND TEXT -- STATIC STUFF
# GROUND
sky_surface = pygame.image.load(f'{path}/graphics/Sky.png').convert()
ground_surface = pygame.image.load(f'{path}/graphics/ground.png').convert()
# TEXT
# text_surface = runner_title.render("Runner", False, (64, 64, 64))
# text_rectangle = text_surface.get_rect(center = (400, 100))

# SNAIL SURFACE/RECTANGLE STUFF
snail_surface = pygame.image.load(f'{path}/graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (900, 300))
# snail_surface_2 = pygame.image.load('graphics/snail/snail2.png')

# PLAYER SURFACE/RECTANGLE STUFF
player_surface = pygame.image.load(f'{path}/graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

player_gravity = 0

while True:     # Entire game will run in this loop; until game is done, the program will stay open
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.bottom == 300 and player_rectangle.collidepoint(event.pos):
                    print("Collided with player")
                    player_gravity = -12.5
            
            if event.type == pygame.KEYDOWN:
                if player_rectangle.bottom == 300 and event.key == pygame.K_SPACE:
                    print("jump")
                    player_gravity = -12.5
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                
        
    if game_active:     # Actual game... the "game" part of the game
        # PLACING STATIC BLOCKS
        screen.blit(sky_surface, (00, 00))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", text_rectangle)
        # pygame.draw.rect(screen, "#c0e8ec", text_rectangle, 10)
        # pygame.draw.line(screen, "Black", (0, 0), pygame.mouse.get_pos())
        # screen.blit(text_surface, text_rectangle)
        
        # SNAIL AND SNAIL MOVEMENT
        screen.blit(snail_surface, snail_rectangle)
        snail_rectangle.x -= 4
        if snail_rectangle.right < -100:
            snail_rectangle.left = 800
        
        # PLAYER SETTING
        player_gravity += 0.4
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        display_score()
        
        screen.blit(player_surface, player_rectangle)
            
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
            score = 0
            
    else:
        screen.fill("Black")
        gameover_surface = test_font.render(f"Game Over! Jump to restart.", False, "White")
        gameover_rectangle = gameover_surface.get_rect(center = (400, 200))
        screen.blit(gameover_surface, gameover_rectangle)

    
    # draw all of the elements
    # update everything
    pygame.display.update()
    clock.tick(60)