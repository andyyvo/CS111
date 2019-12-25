#
# ps6pr3.py - Problem Set 6, Problem 3
#
# Recursive operations on binary numbers
#
# no loops or LCs allowed
#

# 1.

def bitwise_and(b1, b2):
    """ returns the result of the computation of bitwise AND
        on the two binary string numbers b1 and b2 in the form of a string
        uses recursion to compute
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return '0' * len(b2)
    elif b2 == '':
        return '0' * len(b1)
    else:
        bitwise_rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return bitwise_rest + '1'
        else:
            return bitwise_rest + '0'

# 2.

def add_bitwise(b1, b2):
    """ returns the result of adding two binary strings b1 and b2
        uses recursion to perform the bitwise, "elementary-school" addition
        algorithm
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        add_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return add_rest + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return add_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1':
            return add_rest + '1'
        elif b1[-1] == '1' and b2[-1] == '1':
            return add_bitwise(add_rest,'1') + '0'
