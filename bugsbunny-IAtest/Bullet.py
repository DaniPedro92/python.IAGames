from random import randint
from configs import *

class Bullet:
    def __init__(self):
        self.__x = Window.WIDTH
        self.__y = 350
        self.__vel = randint(10, 20)
        self.__img = Skin.BULLET

    def get_vel(self):
        return self.__vel

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

    def move(self):
        self.__x -= self.__vel

    def is_out(self):
        return self.__x < -self.__img.get_width()

    def reshoot(self):
        if self.is_out():
            self.__vel = randint(10, 20)
            self.__x = Window.WIDTH

