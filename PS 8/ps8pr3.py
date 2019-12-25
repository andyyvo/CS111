#
# ps8pr3.py - Problem Set 8, Problem 3
#
# Partner: Olivia Chuang ochuang@bu.edu
#
# Problem sequences with loops
#

# 1.

def double(s):
    """ returns a string from input s with double of each character in that string
    """
    result = ''
    for c in s:
        result += c*2
    return result
        
# 2.

def weave(s1, s2):
    """ returns a new string that is formed by "weaving" together
        the characters in the strings s1 and s2 to create a single string.
        essentially, the new string should alternate characters from the
        two two strings
    """
    result = ''
    len_shorter = min(len(s1), len(s2))
    if s1 == '':
            result = s2
            return result
    if s2 == '':
            result = s1
            return result
    for i in range(len_shorter):
        if len(s1) > len(s2):
            len_difference = s1[len(s2):]
        elif len(s2) > len(s1):
            len_difference = s2[len(s1):]
        else:
            len_difference = ''
        result += s1[i] + s2[i]
    return result + len_difference

# 3.

def square_evens(values):
    """ takes a list of integers called values and returns a new list
        so that all of its even elements are replaced with their squares
        odd elements are left unchanged
    """
    for i in range(len(values)):
        if (values[i] % 2) == 0:
            values[i] **= 2
    # return values

# 4.

def index(elem, seq):
    """ takes as inputs an element 'elem' and sequence 'seq'
        and uses a loop to find a return index of the first
        occurrence of 'elem' in 'seq'
        'seq' can be either a list or string
            if 'seq' is string -> 'elem' is single-character string
            if 'seq' is list -> 'elem' can be any value
    """
    result = 0
    for a in range(len(seq)):
        if elem == seq[a]:
            return result
        else:
            result += 1
    if result == len(seq):
        result -= (len(seq) + 1)
    return result
