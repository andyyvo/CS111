#
# ps12pr2.py  (Problem Set 12, Problem 2)
#
# AI Player for use in Connect Four
#
# do connect_four(Player('X'),Player('O'))
# do connect_four(Player('X'),AIPlayer('O','LEFT'/'RIGHT'/'RANDOM',1-10)
#

import random
from ps12pr1 import *

class AIPlayer(Player):
    """ A class of a more 'intelligent' computer player -
        one that uses techniques from Artificial Intelligence (AI)
        to choose its next move in Connect Four.
        """

# 2.
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object.
            """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

# 3.
    def __repr__(self):
        """ Returns a string representing an AIPlayer object.
            """
        s = ''
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

        return s

# 4.
    def max_score_column(self, scores):
        """ Returns the index of the column with the maximum score.
            If one or more columns are tied for the maximum score,
            the method should apply the called AIPlayer's tie breaking
            strategy to break the tie.
            """
        lst = []
        x = max(scores)
        for i in range(len(scores)):
            if scores[i] == x:
                lst += [i]
        if self.tiebreak == 'LEFT':
            return lst[0]
        elif self.tiebreak == 'RIGHT':
            return lst[-1]
        else:
            return random.choice(lst)

# 5.
    def scores_for(self, b):
        """ Determines the called AIPlayer's scores for the columns in
            the Board object b.
             -1: column is full.
              0: if chosen as next move, would result in a loss at some point
              during the number of moves looked ahead.
            100: if chosen as next move, would result in a win at some point
              during the number of moves looked ahead.
             50: if chosen as next move, would result in neither a win nor loss
              at any point during the number of moves looked ahead.
            """
        scores = [' ' for i in range(b.width)]

        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponentscores = opponent.scores_for(b)
                scores[col] = 100 - max(opponentscores)
                b.remove_checker(col)
        return scores

# 6.
    def next_move(self, b):
        """ Overrides (i.e., replaces) the next_move method that is
            inherited from Player. Rather than asking the user for the next move,
            this version of next_move should return the called
            AIPlayer‘s judgment of its best possible move.
            """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
        
