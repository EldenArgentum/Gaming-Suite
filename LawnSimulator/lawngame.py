import pygame

# init
pygame.init()

# screen size
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Lawn Mowing Simulator 1.0")
icon = pygame.image.load('Graphics/lawn-mower.png')
pygame.display.set_icon(icon)


# Make sure we can exit the game (infinite loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
