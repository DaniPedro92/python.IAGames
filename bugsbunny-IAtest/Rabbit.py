import pygame
from Orientation import Direction
from configs import *

class Rabbit:
    def __init__(self, x, y, genome, net):
        self.__x = x
        self.__y = y
        self.__initial_y = y
        self.__img = Skin.BUGS_BUNNY
        self.__jump_state = None

        #AI
        self.__genome = genome
        self.__net = net
        self.__ignore_bullet = False

    def get_net(self):
        return self.__net

    def add_fitness(self, amount):
        self.__genome.fitness += amount

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def ignore_bullet(self):
        self.__ignore_bullet = True

    def considers_bullet(self):
        self.__ignore_bullet = False

    def successfull_jump(self, bullet):
        if self.__ignore_bullet:
            return False

        if self.__x > bullet.get_x():
            return True

    def out_of_reach(self, bullet):
        if self.__ignore_bullet:
            return False

        return bullet.get_x() - self.__x > 300

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])
        surface.blit(
            Font.MAIN.render(
                F"FT: {self.__genome.fitness}",
                True,
                'white',
                'black'
            ),
            [self.__x, self.__y - 20]
        )

    def move_left(self):
        self.__x -= 5

        if self.__x < 10:
            self.__x = 10

    def move_right(self):
        self.__x += 5

        if self.__x > 1120:
            self.__x = 1120

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def jump(self):
        if self.__jump_state != None:
            return

        self.__jump_state = Direction.RISING

    def update_jump(self):
        if self.__jump_state == Direction.RISING:
            self.__y -= 10
            if self.__y <= 10:
                self.__jump_state = Direction.FALLING
        elif self.__jump_state == Direction.FALLING:
            self.__y += 10
            if self.__y >= self.__initial_y:
                self.__jump_state = None






