import pygame

# init
pygame.init()

# screen size
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Lawn Mowing Simulator 1.0")
icon = pygame.image.load('Graphics/lawn-mower.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load("Graphics/background.png")

# player
playerImg = pygame.image.load('Graphics/gardener.png')
playerX = 10
playerY = 200
playerX_change = 0
playerY_change = 0
colored = []
green = (0, 255, 0)

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))


# Make sure we can exit the game (infinite loop)
running = True
while running:
    screen.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # movement up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    # background
    screen.blit(background, (0, 0))
    # player
    playerY += playerY_change
    playerX += playerX_change

    # boundaries left and right
    if playerX <= 0:
        playerX = 0
    elif playerX >= 672:
        playerX = 672

    # boundaries up and down
    if playerY <= 200:
        playerY = 200
    elif playerY >= 472:
        playerY = 472

    # cant figure out how to leave a trail. in work
    #colored.append((playerX, playerY))
    #for p in colored:
        #pygame.draw.rect(screen, green, rect)
    player(playerX, playerY)


    # constant update
    pygame.display.update()