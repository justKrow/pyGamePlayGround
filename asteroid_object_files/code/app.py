from random import randint, uniform
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
        self.can_shoot = True
        self.shoot_time = None

    def move(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def shoot_laser(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            Laser(laser_group, self.rect.midtop)

    def update(self):
        self.move()
        self.laser_timer()
        self.shoot_laser()


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=pos)
        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (
            round(self.pos.x), round(self.pos.y))  # basic setup


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.image.load(
            '../graphics/meteor.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (
            round(self.pos.x), round(self.pos.y))  # basic setup


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
meteor_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == meteor_timer:
            meteor_y_pos = randint(-150, -50)
            meteor_x_pos = randint(-100, WINDOW_WIDTH+100)
            Meteor(meteor_group, (meteor_x_pos, meteor_y_pos))

    # delta time in seconds
    dt = clock.tick() / 1000

    # background surface
    display_surface.blit(background_surface, (0, 0))

    spaceship_group.update()
    laser_group.update()
    meteor_group.update()

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)

    # draw the frame
    pygame.display.update()
