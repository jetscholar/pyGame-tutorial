import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# setup a player 
player = pygame.Rect((300, 250, 50, 50))

# Game Loop
run = True
while run:
    
    # refresh screen
    screen.fill((0, 0, 0))
    
    # draw a player in red
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0) # move left (x, y)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0) # move right
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1) # move up
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1) # move down
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # screen update
    pygame.display.update()

pygame.quit()