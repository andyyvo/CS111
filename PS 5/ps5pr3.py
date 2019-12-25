#
# ps5pr3.py - Problem Set 5, Problem 3
#
# More algorithm design!
#

# 1.

def index(elem, seq):
    """ returns the index of the first occurence of elem in seq using recursion
        seq can be either a list or a string
        if seq is a string, elem will be a single-character string
        if seq is a list, elem can be any value
    """
    if seq == '' or seq == []:
        return -1
    if elem == seq[0]:
        return 0
    else:
        indexrest = index(elem, seq[1:])
        if indexrest == -1:
            return -1
        else:
            return indexrest + 1
    
# 2.

def index_last(elem, seq):
    """ returns the index of the last occurence of elem in seq
        seq can be either a list or a string
        if seq is a string, elem will be a single-character string
        if seq is a list, elem can be any value
    """
    if seq == '' or seq == []:
        return -1
    if elem != seq[len(seq) - 1]:
        return index_last(elem, seq[0:len(seq) - 1])
    elif elem == seq[len(seq) - 1]:
        return len(seq) - 1

# 3.

def rem_first(elem, string):
    """ removes the first occurrence of elem from the string values
    """
    if string == '':
        return ''
    elif string[0] == elem:
        return string[1:]
    else:
        result_rest = rem_first(elem, string[1:])
        return string[0] + result_rest

def jscore(s1, s2):
    """ returns the Jotto score of s1 compared with s2
        positions and order of shared characters within each string do NOT matter
        repeated letters are counted multiple times, as long as they
        both appear multiple times in both strings
    """
    if s1 == '' or s2 == '':
        return 0
    else:
        jscore_rest = jscore(s1[1:], rem_first(s1[0], s2))
        jscore_rest2 = jscore(s1[1:], s2)
        if s1[0] in s2:
            return 1 + jscore_rest
        else:
            return jscore_rest
