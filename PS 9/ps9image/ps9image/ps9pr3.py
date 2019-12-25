#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

# 1.

def grayscale(pixels):
    """ creates and returns a new 2-D list of pixels for an image
        that is a grayscale version of the original image.
    """
    height = len(pixels)
    width = len(pixels[0])
    newimage = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            pixel = pixels[r][c]
            gray = [brightness(pixel), brightness(pixel), brightness(pixel)]
            newimage[r][c] = gray
    return newimage

# 2.

def fold_diag(pixels):
    """ creates and returns a new 2-D list of pixels for an image
        in which the original image is “folded” along its diagonal.
    """
    height = len(pixels)
    width = len(pixels[0])
    newimage = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            if r > c:
                pixels[r][c] = [255, 255, 255]
                pixel1 = pixels[r][c]
                newimage[r][c] = pixel1
            else:
                pixel2 = pixels[r][c]
                newimage[r][c] = pixel2
    return newimage

# 3.

def mirror_horiz(pixels):
    """ creates and returns a new 2-D list of pixels for an image
        in which the original image is “mirrored” horizontally.
        In other words, the right half of the pixels in each row should be
        replaced by the reversed left half of the pixels from the same row.
    """
    height = len(pixels)
    width = len(pixels[0])
    newimage = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            if c >= (width // 2):
                pixel3 = pixels[r][(width // 2) - (c - (width // 2)) - 1]
                newimage[r][c] = pixel3
            else:
                pixel4 = pixels[r][c]
                newimage[r][c] = pixel4
    return newimage

# 4.

def extract(pixels, rmin, rmax, cmin, cmax):
    """ creates and returns a new 2-D list that represents the portion of the
        original image that is specified by the other four parameters.
        The extracted portion of the image should consist of the pixels
        that fall in the intersection of:
            the rows of pixels that begin with row rmin and go up to but
            not including row rmax.
            the columns of pixels that begin with column cmin and go up to
            but not including column cmax. 
    """
    height = len(range(rmin, rmax))
    width = len(range(cmin, cmax))
    newimage = blank_image(height, width)
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            pixel5 = pixels[r][c]
            newimage[r - rmin][c - cmin] = pixel5
    return newimage
