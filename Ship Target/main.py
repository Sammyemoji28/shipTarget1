
import pgzrun
import random
import itertools

HEIGHT = 400
WIDTH = 400

BLOCKPOS = [(350,50),(350,350),(50,350),(50,50)]
blockPosition = itertools.cycle(BLOCKPOS)

ship = Actor("ship", center = (200,200))
block = Actor("block", center = (50,50))

def draw():
    screen.clear()
    ship.draw()
    block.draw()

def moveBlock():
    animate(block,"bounce_end", duration = 1, pos = next(blockPosition))


def update():
    pass

clock.schedule_interval(moveBlock,2)
pgzrun.go()