from random import randint
from configs import *


class Bubble:
    def __init__(self):
        self.__x = window.WIDTH - 500
        self.__y = 250
        self.__img = img.BUBBLE

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
