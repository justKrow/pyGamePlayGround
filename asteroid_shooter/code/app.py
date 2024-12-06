import pygame
import sys


def laser_update(laser_list, speed):
    for laser in laser_list:
        laser.y -= speed * dt
        if laser.bottom < 0:
            laser_list.remove(laser)


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption('asteroid shooter')
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# importing images
ship_surf = pygame.image.load(
    '../graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

laser_surf = pygame.image.load('../graphics/laser.png').convert_alpha()
laser_list = []

# importing background image
background_surf = pygame.image.load(
    '../graphics/background.png').convert()

# import text
font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, 'white')
text_rect = text_surf.get_rect(midbottom=(
    WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))
test_surface = pygame.Surface((200, 100))

# drawing
test_rect = pygame.Rect(500, 100, 50, 50)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('shoot laser')
            laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
            laser_list.append(laser_rect)

    # framerate limit
    dt = clock.tick(120) / 1000  # limit the frame rate to 60 frames per second
    ship_rect.center = pygame.mouse.get_pos()

    # 2. updates
    laser_update(laser_list, 300)
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(text_surf, text_rect)

    # rect drawing
    pygame.draw.rect(display_surface, "white",
                     text_rect.inflate(30, 30), width=4, border_radius=10)
    display_surface.blit(ship_surf, ship_rect)

    for laser in laser_list:
        display_surface.blit(laser_surf, laser)

    # 3. show the frame to the player / update the display surface
    pygame.display.update()
