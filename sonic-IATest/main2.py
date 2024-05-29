import math
import os
import pygame
from pygame.locals import *
import neat
from configs import *
from hero import Hero
from enemy import Enemy
from bubble import Bubble

screen = window.create()
pygame.init()

gen = 0

clock = pygame.time.Clock()


def eval_game(genomes, config):
    global gen, screen, clock

    scroll = 0

    gen += 1

    enemy = Enemy()
    bubble = Bubble()
    sonics = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        sonics.append(Hero(0, 360, genome, net))

    while len(sonics) > 0:
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
                pygame.quit()

        enemy.move()
        enemy.draw(screen)

        for sonic in sonics:
            output = sonic.get_net().activate(
                (
                    sonic.get_x(),
                    sonic.get_y(),
                    enemy.get_x(),
                    enemy.get_y(),
                    bubble.get_x(),
                    bubble.get_y(),
                )
            )

            # 0 0
            move_left = output[0] > 0
            move_right = output[1] > 0
            move_jump = output[2] > 0

            if move_left:
                sonic.move_left()
            elif move_right:
                sonic.move_right()

            if move_jump:
                sonic.jump()

            if sonic.colides_with(enemy):
                sonic.add_fitness(-20)
                sonics.remove(sonic)
                continue

            '''if sonic.get_x() < 250:  # 500
                sonic.add_fitness(-10)
            elif sonic.get_x() < 400 and sonic.get_x() >= 250:
                sonic.add_fitness(10)
            elif sonic.get_x() < 500 and sonic.get_x() >= 400:
                sonic.add_fitness(50)'''

            if sonic.colides_with(bubble):
                sonic.add_fitness(100) #TODO adicionar um else para testar

            # uncessaru_jump
            if move_jump and sonic.out_of_reach(enemy):
                sonic.add_fitness(-10)

            if sonic.successfull_jump(enemy):
                sonic.ignore_enemy()
                if sonic.get_x() < 600:
                    sonic.add_fitness(10)
                else:
                    sonic.add_fitness(-5)

            if enemy.is_out():
                sonic.considers_enemy()

            sonic.update_jump()
            sonic.draw(screen)
            bubble.draw(screen)

        if enemy.is_out():
            enemy.reshoot()

        pygame.display.update()


config_file = os.path.join(os.path.dirname(__file__), 'neat-config.txt')
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                            neat.DefaultStagnation, config_file)

population = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)

winner = population.run(eval_game, 9999)
print('\nBest genome:\n{!s}'.format(winner))

pygame.quit()
