import pygame
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption('asteroid shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# importing images
ship_surf = pygame.image.load(
    '../graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# importing background image
background_surf = pygame.image.load(
    '../graphics/background.png').convert()

# import text
font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'white')
text_rect = text_surf.get_rect(midbottom=(
    WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))

# create a surface
test_surface = pygame.Surface((200, 100))
# we need to attach the surface to the display surface


while True:  # run forever -> keeps our game running
    # Do not run the code until i tell you

    # 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)  # limit the frame rate to 60 frames per second

    # 2. updates
    # draw the surface on the display surface
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surf, (0, 0))
    if ship_rect.y > 0:
        # print(ship_rect.y)
        ship_rect.y -= 4
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)

    # 3. show the frame to the player / update the display surface
    pygame.display.update()
