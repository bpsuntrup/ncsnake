from enum import Enum
from itertools import chain
from operator import add

# Utils:
def chomp(iter):
    """ Returns an iterator sans the last item in iter
    TODO: test this """

    # Get first element 
    try:
        first = next(iter)
    except StopIteration:
        raise StopIteration

    # Get second element
    try:
        second = next(iter)
    except StopIteration:
        # Don't yield anything if there was only one element
        raise StopIteration

    # Safe now to yield first
    yield first

    while True:
        first = second
        second = next(iter)
        yield first

class Direction(Enum):
    """ Use the values in this direction type to calculate the next position
    of the snake's head"""
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

def advance(snake, direction):
    ''' Takes a list of positions (snake) and returns a snake advanced in the
    direction given of type Direction'''
    return chain([tuple(map(add, snake[0], direction))], chomp(iter(snake)))
    
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
    list(map(print, advance(snake, (0,1))))
    print('mapaddsnake0direction:')
    print(tuple(map(add,snake[0],(0,1))))

