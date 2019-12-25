# 
# ps2pr1.py - Problem Set 2, Problem 1
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def cube(x):
    """ returns the cube of its input
        input x: any number (int or float)
    """
    return x**3

# function 2
def convert_to_inches(yards,feet):
    """ returns the conversion of inches of two numeric inputs that together represent a single length broken up into yards and feet
        input yards and feet: any number (int or float)
    """
    if yards < 0:
        yards = 0
    if feet < 0:
        feet = 0
    a = 36 * yards
    b = 12 * feet
    return a+b

# function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """ returns the area of a rectangle in square inches by determining height and width of rectangle in inches, then returning the product of those two values
        input height_yds, height_ft, width_yds, width_ft: any number (int or float)
    """
    if height_yds < 0:
        height_yds = 0
    if height_ft < 0:
        height_ft = 0
    if width_yds < 0:
        width_yds = 0
    if width_ft < 0:
        width_ft = 0
    a = 36 * height_yds
    b = 12 * height_ft
    c = 36 * width_yds
    d = 12 * width_ft
    height_in = a + b
    width_in = c + d
    return height_in * width_in

# function 4
def median(a,b,c):
    """ returns the median of the three inputs (the value that falls in the middle of the other two when the three values are listed in increasing order)
        input a,b,c: any number (int or float)
    """
    if b <= a <= c:
        return a
    elif c <= a <= b:
        return a
    elif a <= b <= c:
        return b
    elif c <= b <= a:
        return b
    elif a <= c <= b:
        return c
    elif b <= c <= a:
        return c

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
