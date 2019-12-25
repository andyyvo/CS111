#
# ps5pr1.py - Problem Set 5, Problem 1
#
# Algorithm Design
#

#
# 1. cube all values function with LC
#

def cube_all_lc(values):
    """ returns a list containing the cubes of the numbers in 'values'
        using List Comprehension
    """
    cubedlc_values = [x**3 for x in values]
    return cubedlc_values

#
# 2. cube all values function with recursion
#

def cube_all_rec(values):
    """ returns a list containing the cubes of the numbers in 'values'
        using Recursion
    """
    if values == []:
        return []
    else:
        cubedrec_values = cube_all_rec(values[1:])
        return [values[0]**3] + cubedrec_values

#
# 3. numbers larger than certain threshold value function
#

def num_larger(threshold,values):
    """ returns the number of elements of 'values' that are larger than 'threshold'
        using either LC or recursion
    """
    if values == []:
        return 0
    else:
        num_rest = num_larger(threshold,values[1:])
        if values[0] > threshold:
            return 1 + num_rest
        else:
            return num_rest

#
# 4. word with the most consonants in a list function
#

def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_consonants(words):
    """ returns the string in the list with the most consonants
    """
    consonants = [[len(x) - num_vowels(x),x] for x in words]
    maxconsonants = max(consonants)
    return maxconsonants[1]

#
# 5. converting cents to dollars and cents function
#

def price_string(cents):
    """ returns a string  in which the price is expressed as a combination
        of dollars and cents that takes as input a positive integer 'cents'
        representing a price given in cents
    """
    if cents < 100:
        if cents == 1:
            return '1 cent'
        else:
            cents = str(cents)
            return cents + ' cents'
    elif cents >= 100:
        dollars = cents // 100
        if cents % 100 == 0 and dollars == 1:
            dollars = str(dollars)
            return '1 dollar'
        elif cents % 100 == 0 and dollars > 1:
            dollars = str(dollars)
            return dollars + ' dollars'
        else:
            cents = cents % 100
            if cents == 1:
                if dollars == 1:
                    dollars = str(dollars)
                    return '1 dollar, 1 cent'
                else:
                    dollars = str(dollars)
                    return dollars + ' dollars, ' + '1 cent'
            else:
                if dollars == 1:
                    dollars = str(dollars)
                    cents = str(cents)
                    return '1 dollar, ' + cents + ' cents'
                else:
                    cents = str(cents)
                    dollars = str(dollars)
                    return dollars + ' dollars, ' + cents + ' cents'

def price_string(cents):
    """ returns a string  in which the price is expressed as a combination
        of dollars and cents that takes as input a positive integer 'cents'
        representing a price given in cents
    """
    d = cents // 100 #dollars
    c = cents % 100 #cents remaining
    price = ''
    if d == 0:
        if c == 0:
            price = ''
        elif c == 1:
            price = '1 cent'
        else:
            price = str(c) + ' cents'
    elif d == 1:
        if c == 0:
            price = '1 dollar'
        elif c == 1:
            price = '1 dollar, 1 cent'
        else:
            price = '1 dollar, ' + str(c) + ' cents'
    else:
        if c == 0:
            price = str(d) + ' dollars'
        elif c == 1:
            price = str(d) + ' dollars, 1 cent'
        else:
            price = str(d) + ' dollars, ' + str(c) + ' cents'
    return price
