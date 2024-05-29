import os
import pygame
from pygame.locals import *
import neat
from configs import *
from Rabbit import Rabbit
from Bullet import Bullet

screen = Window.create()
pygame.init()

gen = 0

clock = pygame.time.Clock()

def eval_game(genomes, config):
    global gen, screen, clock

    gen += 1

    bullet = Bullet()
    bugs_bunnies = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        bugs_bunnies.append(Rabbit(500, 200, genome, net))

    while len(bugs_bunnies) > 0:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(World.BACKGROUND, [0, 0])

        bullet.move()
        bullet.draw(screen)

        for bugs_bunny in bugs_bunnies:
            output = bugs_bunny.get_net().activate(
                (                   bullet.get_vel(),
                    bugs_bunny.get_x(),
                    bugs_bunny.get_y(),
                    bullet.get_x(),
                    bullet.get_y(),
                )
            )

            #0 0
            move_left = output[0] > 0
            move_right = output[1] > 0
            move_jump = output[2] > 0

            if move_left:
                bugs_bunny.move_left()
            elif move_right:
                bugs_bunny.move_right()

            if move_jump:
                bugs_bunny.jump()

            if bugs_bunny.colides_with(bullet):
                bugs_bunny.add_fitness(-20)
                bugs_bunnies.remove(bugs_bunny)
                continue

                                #"unceressary_jumped"
            if move_jump and bugs_bunny.out_of_reach(bullet):
                bugs_bunny.add_fitness(-10)

            if bugs_bunny.successfull_jump(bullet):
                bugs_bunny.ignore_bullet()

                if bugs_bunny.get_x() < 600:
                    bugs_bunny.add_fitness(10)
                else:
                    bugs_bunny.add_fitness(-5)

            if bullet.is_out():
                bugs_bunny.considers_bullet()

            bugs_bunny.update_jump()
            bugs_bunny.draw(screen)


        if bullet.is_out():
            bullet.reshoot()

        pygame.display.update()

config_file = os.path.join(os.path.dirname(__file__), 'neat-config.txt')
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)

population = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)

winner = population.run(eval_game, 9999)
print('\nBest genome:\n{!s}'.format(winner))

pygame.quit()