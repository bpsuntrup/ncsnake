from enum import Enum, IntEnum
import shutil
import time
from itertools import chain, starmap
from functools import partial
from operator import add
from utils import NCurses, apply, chomp, unzip, constantly


class Direction(Enum):
    """ Use the values in this direction type to calculate the next position
    of the snake's head"""
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

def advance(snake, direction, food):
    """ Takes a list of positions (snake) and returns a snake advanced in the
    direction given of type Direction. Snake "grows" if it eats food

    snake must be a list """

    return \
    apply(
        lambda x:
            chain(
                [x],
                chomp(iter(snake)) if not x == food else iter(snake)),
        tuple(
            map(
                add,
                snake[0],
                direction.value)))

def check_snake(snake, direction, boundary):
    ''' Returns true if snake may proceed in given direction without eating
    itself or falling off the world, False otherwise'''
    return \
    not apply(
        lambda x: x in snake or x in boundary,
        tuple(map(add, snake[0], direction.value)))

def undraw(window, container):
    """Undraws everything in container"""

def draw_snake(nc, window, snake):
    """Draws everything blue in window in container. Containert must be a 
    list"""
    print("DUUUUDE")
    starmap(window.addstr, apply(partial(zip, *unzip(iter(snake))), constantly(' '), constantly(nc.color_pair(4))))
    window.refresh()

    
if __name__ == '__main__':

    snake = [(6,6), (6,7), (6,8)]

    with NCurses() as nc:
        class Color(IntEnum):
            RW = 1
        # Pick colors I like:
        nc.init_pair(1, nc.COLOR_RED, nc.COLOR_WHITE)
        nc.init_pair(2, nc.COLOR_WHITE, nc.COLOR_RED)
        nc.init_pair(3, nc.COLOR_BLUE, nc.COLOR_WHITE)
        nc.init_pair(4, nc.COLOR_BLUE, nc.COLOR_BLUE)
        nc.init_pair(5, nc.COLOR_GREEN, nc.COLOR_BLACK)
        nc.init_pair(6, nc.COLOR_BLACK, nc.COLOR_WHITE)

        # Draw a new window... I guess
        cols, rows = shutil.get_terminal_size()
        x = 1
        y = 1
        height = rows-2
        width = cols-2
        # win = nc.newwin(height, width, y, x)
        win = nc.newwin(height, width, y, x)
        win.timeout(200)
        win.addstr(2, 20, 'READY', nc.color_pair(3))
        draw_snake(nc, win, snake)
        win.refresh()
        time.sleep(2)
        win.addstr(4,20,'GO', nc.color_pair(2))
        win.refresh()
