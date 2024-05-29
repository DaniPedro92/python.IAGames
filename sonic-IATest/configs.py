import pygame
pygame.init()

class window:
    WIDTH = 1000
    HEIGHT = 450
    TITLE = "Mario Game Test"
    ICON = pygame.image.load("imgs/background.jpg")

    @staticmethod
    def create():
        screen = pygame.display.set_mode((window.WIDTH, window.HEIGHT))
        pygame.display.set_caption(window.TITLE)
        pygame.display.set_icon(window.ICON.convert_alpha())
        pygame.event.set_allowed([pygame.QUIT])  # associar à janela apenas o evento de [x] (fechar)

        return screen


class img:
    BACKGROUND = pygame.image.load("imgs/background.jpg")
    SONIC = pygame.image.load("imgs/sonic.png")
    ENEMY = pygame.image.load("imgs/enemy.png")
    BUBBLE = pygame.image.load("imgs/bubble.png")


class font:
    MAIN = pygame.font.Font("fonts/Roboto-Regular.ttf", 20)
