#
# ps3pr5.py - Problem Set 3, Problem 5
#
# Fun with recursion, part II
#

# 1.

def letter_score(letter):
    """ returns the value of a lowercase letter from a to z as a scrabble tile.
        otherwise, the return is 0.
    """
    assert(len(letter) == 1)
    if letter in ['a','e','i','l','n','o','r','s','t','u']:
        return 1
    elif letter in ['d','g']:
        return 2
    elif letter in ['b','c','m','p']:
        return 3
    elif letter in ['f','h','v','w','y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j','x']:
        return 8
    elif letter in ['q','z']:
        return 10
    else:
        return 0

# 2. using scrabble to score function with recursion

def scrabble_score(word):
    """ returns the scrabble score of the string (the sume of the scrabble score
        of its letters.
    """
    if word == '':
        return 0
    else:
        word_rest = word[1:]
        return letter_score(word[0]) + scrabble_score(word_rest)

# 3. adding lists with recursion

def add(vals1,vals2):
    """ returns a new list in which each element is the sum of the corresponding elements
        of vals1 and vals2.
        assume that both lists are of the same length.
    """
    if len(vals1) == len(vals2) == 0:
        return []
    else:
        add_rest = add(vals1[1:],vals2[1:])
        return [vals1[0] + vals2[0]] + add_rest

# 4. weaving recursion function

def weave(s1,s2):
    """ returns a new string that will alternate characters from the two strings
    """
    if len(s1) == 0 and len(s2) == 0:
        return ''
    elif len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        weave_rest = weave(s1[1:],s2[1:])
        return s1[0] + s2[0] + weave_rest
