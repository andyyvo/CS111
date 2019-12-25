#
# ps12pr1.py  (Problem Set 12, Problem 1)
#
# Playing the game
#

from ps11pr1 import Board
from ps11pr2 import Player
import random

def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
        players (objects of the Player class or a subclass of Player).
        One player should use 'X' checkers and the other should
        use 'O' checkers.
        """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
        or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)

    while True:
        if process_move(p1, b) == True:
            return b
        
        if process_move(p2, b) == True:
            return b

# 1.
def process_move(p, b):
    """ The function will perform all of the steps involved in
        processing a single move by player p on board b.
        """
    print(p, "'s turn")
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    print()
    if b.is_win_for(p.checker) == True:
        print(p.__repr__() + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

# 2.
class RandomPlayer(Player):
    """ class for 'unintelligent' computer player that chooses at random
        from the available columns.
        This is a subclass of the Player class implemented in ps11pr2.
        """
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is
            inherited from Player.
            """
        lst = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                lst += [col]
            else:
                lst
        return random.choice(lst)
