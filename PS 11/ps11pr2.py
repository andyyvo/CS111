#
# ps11pr2.py (Problem Set 11, Problem 2)
#
# A Connect Four Player class 
#

from ps11pr1 import Board

# Write your class below.

class Player:
    """ A class that uses class Board objects and their methods
        to represent a player of the Connect Four game, enabling
        one to play with another.
        """

# 1.
    # constructor
    def __init__(self, checker):
        """ constructor that initializes the attributes in every
            Player object.
            checker -  a one-character string that represents the
                gamepiece for the player, as specified by the parameter checker.
            num_moves – an integer that stores how many moves the
                player has made so far.
            """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0

# 2.
    # return string
    def __repr__(self):
        """ Returns a string representation for a Board object.
            """
        s = ''
        s += 'Player ' + str(self.checker)

        return s

# 3.
    # opponent checker
    def opponent_checker(self):
        """ Returns a one-character string representing the checker
            of the Player object's opponent.
            """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

# 4.
    # most important method here
    def next_move(self, b):
        """ Returns the column where the player wants to make the next move.
            """
        self.num_moves += 1

        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == False:
                print('Try again!')
            else:
                break
        return col
