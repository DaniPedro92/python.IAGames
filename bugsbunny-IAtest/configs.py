import pygame
from pygame.locals import *

pygame.init()

# sugestões para optimização
# https://www.codeproject.com/Articles/5298051/Improving-Performance-in-Pygame-Speed-Up-Your-Game

class Window:
    WIDTH = 1250
    HEIGHT = 467
    TITLE = "Looney Tunes"
    ICON = pygame.image.load("imgs/icon.png")

    @staticmethod
    def create():
        screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption(Window.TITLE)
        pygame.display.set_icon(Window.ICON.convert_alpha())
        pygame.event.set_allowed([QUIT])  # associar à janela apenas o evento de [x] (fechar)

        return screen


# criar temporariamente uma janela para que a conversão de imagens abaixo funcione
pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))


class World:
    GROUND_POSITION = 390
    BACKGROUND = pygame.image.load("imgs/fundo.png").convert()

    """class Gameover:
        IMG = pygame.image.load("../LooneyTunes/imgs/gameover.png").convert_alpha()
        X = Window.WIDTH / 2 - IMG.get_width() / 2
        Y = Window.HEIGHT / 2 - IMG.get_height() / 2"""


class Skin:
    BUGS_BUNNY = pygame.image.load("imgs/coelho.png").convert_alpha()
    ELMER = pygame.image.load("imgs/cacador.png").convert_alpha()
    BULLET = pygame.image.load("imgs/bullet.png").convert_alpha()
    HEART = pygame.image.load("imgs/heart.png").convert_alpha()
    CARROTS = [
        pygame.image.load("imgs/cenoura1.png").convert_alpha(),
        pygame.image.load("imgs/cenoura2.png").convert_alpha(),
        pygame.image.load("imgs/cenoura3.png").convert_alpha(),
        pygame.image.load("imgs/cenoura4.png").convert_alpha(),
    ]

class Font:
    MAIN = pygame.font.Font('fonts/Roboto-Regular.ttf', 20)
