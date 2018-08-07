from enum import Enum
from itertools import chain
from operator import add
from utils import NCurses, apply, chomp


class Direction(Enum):
    """ Use the values in this direction type to calculate the next position
    of the snake's head"""
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

def advance(snake, direction, food):
    ''' Takes a list of positions (snake) and returns a snake advanced in the
    direction given of type Direction. Snake "grows" if it eats food'''
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

    
if __name__ == '__main__':
    for i in chomp(iter([1,2,3,4,5])):
        print(i)
    for i in chomp(iter([4,5])):
        print(i)
    for i in chomp(iter([5])):
        print(i)

    snake = [(0,0), (0,1), (0,2)]
    list(map(print, snake))
    list(map(print, chomp(iter(snake))))
    list(map(print, advance(snake, Direction.EAST, (0,1))))
    print('mapaddsnake0direction:')
    print(tuple(map(add,snake[0],(0,1))))

