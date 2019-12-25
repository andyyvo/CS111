# problem 3: functions on strings and lists, part 1
#
# 1. finding first and last values in a list
#

def first_and_last(values):
    """function takes list (values) and returns new list with first and last values of original list"""
    first = values[0]
    last = values[-1]
    return [first, last]

#
# 2. counting length of longer string value
#

def longer_len(s1,s2):
    """returns length of longer string inputted"""
    if len(s1) >= len(s2):
        return len(s1)
    else:
        return len(s2)

#
# 3. moving sliced section of string value to end of sliced word based on integer input
#

def move_to_end(s,n):
    if n >= len(s):
        return s
    else:
        sliced = s[0:n]
        nonsliced = s[n:]
        return nonsliced + sliced
