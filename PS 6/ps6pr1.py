#
# ps6pr1.py - Problem Set 6, Problem 1
#
# From binary to decimal and back!
#

# 1.

def dec_to_bin(n):
    """ returns a string of the binary representation of integer number n
        function uses recursion and does not use loops or LCs
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n < 0:
        return 'n must be a positive integer'
    else:
        return dec_to_bin(n//2) + str(n % 2)

# 2.

def bin_to_dec(n):
    """ returns the integer of the binary string input n
        function uses recursion and no loops/LCs
    """
    if n == '0':
        return 0
    elif n == '1':
        return 1
    else:
        bindec_rest = bin_to_dec(n[:-1]) * 2
        return bindec_rest + int(n[-1])
