from visual import *
from RobotsAndZombies import *
import random
import math

GROUND_RADIUS = 50
ZOMBIES = 20

def makeZombies():
    zombies = []
    for z in range(ZOMBIES):
        theta = random.uniform(0, 360)
        r = random.uniform(0, GROUND_RADIUS)
        x = r * cos(math.radians(theta))
        z = r * sin(math.radians(theta))
        zombies.append(ZombieBot(position = vector(x, 0, z)))
    return zombies

def main():
    ground = cylinder(pos = (0, -1, 0), axis = (0, 1, 0), radius = GROUND_RADIUS)
    player = PlayerBot()
    zombies = makeZombies()
    while True:
        rate(30)
        player.update()
        if mag(player.location) >= GROUND_RADIUS:
            player.turn(180)
        for z in zombies:
            z.update()
            if mag(z.location) >= GROUND_RADIUS:
                z.turn(random.uniform(150, 210))


main()