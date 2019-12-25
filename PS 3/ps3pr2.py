#
# ps3pr2.py - Problem Set 3, Problem 2
#
# More practice writing non-recursive functions
#

# 1. flipside function

def flipside(s):
    """ returns a string whose first half is s's second half
        and whose second half is s's first half.
        If len(s) is odd, first half of input string should have one fewer character
        than second half.
    """
    firsthalf_len = len(s) // 2
    return s[firsthalf_len:] + s[:firsthalf_len]


# 2. adjusting length of string function

def adjust(s,length):
    """ returns a string in which the value of s has been adjusted as neccesary
        to produce a string with specified 'length'.
        If s is too short, value that is returned should be 'padded' with spaces
        on the left-hand side.
        If s is correct length or too long, returned value should be the first 'length'
        characters of s.
    """
    if length <= len(s):
        return s[:length]
    else:
        a = length - len(s)
        return (a*' ') + s
