import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption('asteroid shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


while True:  # run forever -> keeps our game running
    # Do not run the code until i tell you

    # 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. updates
    # nothing yet :)

    # 3. show the frame to the player / update the display surface
    pygame.display.update()
