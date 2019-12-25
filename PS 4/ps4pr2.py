#
# ps4pr2.py - Problem Set 4, Problem 2
#
# list comprehensions
#

# Problem 2-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [2*x for x in range(5)]

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]

# part c
lc3 = [2*word[::-1] for word in ['hello', 'bye', 'no']]

# part d
lc4 = [x**2 for x in range(1, 10) if x % 2 == 0]

# part e
lc5 = [c in ['b','u'] for c in 'bu be you']


# Problem 2-2: Put your definition of the function below.

def powers_of(base,count):
    """ returns a list containing the first 'count' powers of 'base'
        beginning with the 0th power.
    """
    lc_powers = [base**x for x in range(count)]
    return lc_powers

# Problem 2-3: Put your definition of the function below.

def shorter_than(n,wordlist):
    """ returns a list consisting of all words from wordlist that are shorter than n.
    """
    lc_short = [x for x in wordlist if len(x) < n]
    return lc_short

# The code below prints the values of your expressions
# from 2-1. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(1, 6):
        lc_var = 'lc' + str(n)
        if lc_var in dir():
            print(lc_var, '=', eval(lc_var))
