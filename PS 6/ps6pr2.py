#
# ps6pr2.py - Problem Set 6, Problem 2
#
# Using your conversion functions
#

from ps6pr1 import *

# 1.

def add(b1, b2):
    """ returns the sum of binary string values b1 and b2 as a new binary string
    """
    b1 = bin_to_dec(b1)
    b2 = bin_to_dec(b2)
    total = b1 + b2
    return dec_to_bin(total)

# 2.

def increment(b):
    """ returns the next larger binary number of an 8-character binary string
    """
    if b == '11111111':
        return '00000000'
    else:
        binnew = bin_to_dec(b)
        decnew = binnew + 1
        binnew1 = dec_to_bin(decnew)
        if len(binnew1) < 8:
            newlen = 8 - len(binnew1)
            return '0' * newlen + binnew1
        else:
            return binnew1
