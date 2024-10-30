import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption('asteroid shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# create a surface
test_surface = pygame.Surface((400, 100))
# we need to attach the surface to the display surface


while True:  # run forever -> keeps our game running
    # Do not run the code until i tell you

    # 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. updates
    # draw the surface on the display surface
    display_surface.fill((95, 191, 167))
    test_surface.fill((182, 62, 111))
    display_surface.blit(test_surface, (0, 0))

    # 3. show the frame to the player / update the display surface
    pygame.display.update()
