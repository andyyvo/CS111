#
# ps8pr4.py - Problem Set 8, Problem 4
#
# Partner: Olivia Chuang ochuang@bu.edu
#
# Definite vs. Indefinite loops
#

# 1.

def log(b, n):
    """ uses a loop to compute and return the logarithm to the base 'b' of a number 'n'
        in cases in which n is not an integral power of 'b',
        return an integer estimate of the log
    """
    # ex: log(10, 1000) is 3 because 10**3 is 1000
    # ex: log (2, 32) is 5 because 2**5 is 32
    result = 0
    while n > 1:
        result += 1
        print('dividing ' + str(n) + ' by ' + str(b) + ' gives ' + str(n // b))
        n //= b
    return result

# 2.

def add_powers(m, n):
    """ takes a positive integer 'm; and an arbitrary integer 'n'
        uses loop to add together the first m powers of n
        (from n**0 up to and including n**(m-1)power)
        and returns the resulting sum
    """
    total = 0
    for i in range(m):
        print(str(n) + ' ** ' + str(i) + ' = ' + str(n**i))
        total += n**i
    return total
