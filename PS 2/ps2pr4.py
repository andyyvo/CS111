#
# problem 4: functions on strings and lists, part 2
#
# 1. mirror function
#

def mirror(s):
    """returns a mirrored version of that is twice the length of the original string."""
    mirror = s[::-1]
    return s + mirror

#
# 2. is the string a mirrored string function
#

def is_mirror(s):
    """ returns a boolean value
        True if string is mirrored; False if string is not mirrored."""
    firsthalf = len(s) // 2
    secondhalf = (-1 * firsthalf) - 1
    return s[:firsthalf] == s[:secondhalf:-1]

#
# 3. replace values function
#

def replace_end(values, new_end_vals):
    """ returns a new list in which the elements in new_end_vals have replaced the last n elements of the list values.
        n is the length of new_end_vals."""
    n = len(new_end_vals)
    #print(values[0:n])
    if n >= len(values):
        return new_end_vals
    elif n == 0:
        return values
    else:
        return values[:-n] + new_end_vals

#
# 4. repeating elements in a list function
#

def repeat_elem(values, index, num_times):
    """ returns a new list where the element of values at position 'index' has been repeated 'num_times'.
        index and num_times are integer values."""
    i = index
    n = num_times
    return values[0:i] + n*[values[i]] + values[i+1:]
