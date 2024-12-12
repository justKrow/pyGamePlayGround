import pygame
import sys


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        # init the sprite(parent) class
        super().__init__(groups)
        # need a surface -> image for the class
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()
        # need a rect for the class
        self.rect = self.image.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=pos)


# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('space shooter')
clock = pygame.time.Clock()

# background surface
background_surface = pygame.image.load(
    '../graphics/background.png').convert_alpha()

# sprite group
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group, (500, 100))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time in seconds
    dt = clock.tick() / 1000

    # background surface
    display_surface.blit(background_surface, (0, 0))

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)

    # draw the frame
    pygame.display.update()
