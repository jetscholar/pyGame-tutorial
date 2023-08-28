import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Gam Loop
run = True
while run:
    
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()