import pygame
import sys
from random import randint, uniform


def laser_update(laser_list, speed):
    for laser in laser_list:
        laser.y -= speed * dt
        if laser.bottom < 0:
            laser_list.remove(laser)


def meteor_update(meteor_list, speed):
    for meteor in meteor_list:
        direction = meteor[1]
        meteor_rect = meteor[0]
        meteor_rect.center += direction * speed * dt
        # meteor.y += speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor)


def laser_timer(can_shoot, duration):
    current_time = pygame.time.get_ticks()
    if can_shoot == False:
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot


def display_score():
    score_text = f'Score: {pygame.time.get_ticks()//1000}'
    text_surf = font.render(score_text, True, 'white')
    text_rect = text_surf.get_rect(midbottom=(
        WINDOW_WIDTH // 2, WINDOW_HEIGHT - 80))
    test_surface = pygame.Surface((200, 100))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, "white",
                     text_rect.inflate(30, 30), width=4, border_radius=10)


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

# drawing
test_rect = pygame.Rect(500, 100, 50, 50)

can_shoot = True
shoot_time = None

# meteor
meteor_surf = pygame.image.load(
    '../graphics/meteor.png').convert_alpha()
meteor_list = []
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 1000)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            print('shoot laser')
            laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH+100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(center=(x_pos, y_pos))
            # direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rect, direction))
            print('meteor appears')

    can_shoot = laser_timer(can_shoot, 500)
    # framerate limit
    dt = clock.tick(120) / 1000  # limit the frame rate to 60 frames per second
    ship_rect.center = pygame.mouse.get_pos()

    # 2. updates
    pygame.time.get_ticks()
    laser_update(laser_list, 300)
    meteor_update(meteor_list, 300)
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surf, (0, 0))
    display_score()

    display_surface.blit(ship_surf, ship_rect)

    for laser in laser_list:
        display_surface.blit(laser_surf, laser)

    for meteor in meteor_list:
        display_surface.blit(meteor_surf, meteor[0])

    # 3. show the frame to the player / update the display surface
    pygame.display.update()
