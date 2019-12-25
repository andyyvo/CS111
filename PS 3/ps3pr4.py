#
# ps3pr4.py - Problem Set 3, Problem 4
#
# Fun with recursion, part I

# 1. copy function with recursion

def copy(s,n):
    """ returns a string in which n copies of s have been concatenated together.
    """
    if n <= 0:
        return ''
    else:
        copy_rest = copy(s,n-1)
        return s + copy_rest

# 2. compare list function

def compare(list1,list2):
    """ returns the number of values in list1 that are smaller than their corresponding
        index value in list2.
        e.g. compares list1[0] with list2[0]
    """
    b = len(list2)
    if len(list1) == 0:
        return 0
    elif b == 0:
        return 0
    else:
        compare_rest1 = list1[1:b]
        compare_rest2 = list2[1:b]
        if list1[0] < list2[0]:
            return 1 + compare(compare_rest1,compare_rest2)
        else:
            return 0 + compare(compare_rest1,compare_rest2)

# 3. double each letter function

def double(s):
    """ returns the string s by doubling each character in the string
    """
    if s == '':
        return ''
    else:
        double_rest = s[1:]
        return 2*s[0] + double(double_rest)
