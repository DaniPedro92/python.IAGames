import math
import pygame
from configs import *
from hero import Hero
from enemy import Enemy

pygame.init()
screen = window.create()

gen = 0

scroll = 0

clock = pygame.time.Clock()

sonic = Hero(0, 360)
enemy = Enemy()

run = True
while run:
    dt = clock.tick(60)

    bg = img.BACKGROUND.convert()
    bg_width = bg.get_width()
    tiles = math.ceil(window.WIDTH / bg_width) + 1

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 4

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    enemy.move()
    enemy.draw(screen)

    if enemy.is_out():
        enemy.reshoot()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sonic.move_left()
    elif key[pygame.K_RIGHT]:
        sonic.move_right()

    if key[pygame.K_SPACE]:
        sonic.jump()

    sonic.update_jump()
    sonic.draw(screen)

    screen.blit(img.BUBBLE, ((window.WIDTH - 100, 270)))
    #screen.blit(img.SONIC, (0, 360))
    #screen.blit(img.ENEMY, (200, 365))
    pygame.display.update()
