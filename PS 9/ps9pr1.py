#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Olivia Chuang
# partner's email: ochuang@bu.edu
# 

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

# 0.

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

# 1.

def inner_grid(height, width):
    """ creates and returns a 2-D list of 'height' rows and 'width' columns
        in which the "inner" cells are all 1 and the calle on the outer
        border ae all 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s here too

    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = 1

    return grid

# 2.

def random_grid(height, width):
    """ creates and returns a 2-D list of 'height' rows and 'width' columns
        in which the inner cells are randomly assigned either 0 or 1, but the
        cells on the outer border are all 0.
        inputs: height and width are non-negative numbers
    """
    grid = create_grid(height, width)

    for r in range(1, height - 1):
        for c in range(1, width - 1):
            grid[r][c] = random.choice(range(2))

    return grid

# 3.

def copy(grid):
    """ creates and returns a deep copy of 'grid' - a new, separate 2-D list
        with the same dimensions and cell values as 'grid'.
    """
    newgrid = create_grid(len(grid), len(grid[0]))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            newgrid[r][c] = grid[r][c]

    return newgrid

# 4.

def invert(grid):
    """ takes an existing 2-D list of 0s and 1s and inverts it,
        which changes all 0 values to 1, and all 1 values to 0.
    """

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                grid[r][c] = 1
            else:
                grid[r][c] = 0
