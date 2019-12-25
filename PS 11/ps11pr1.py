#
# ps11pr1.py - Problem Set 11, Problem 1
#
# A Connect Four Board class
#
# Partner: Olivia Chuang
# Partner's email: ochuang@bu.edu
#

class Board:
    """ A class that stores and manipulates pieces that are
        utilized to play game of Connect Four with arbitrary dimensions.
        """

# 1.
    # constructor
    def __init__(self, height, width):
        """ constructor that initializes the two attributes in every
            Board object (height and width).
            """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

# 2.
    # string returner
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        for col in range(self.width):
            s += '--'
        s += '-'
        s += '\n' # another newline
    
        # and the numbers underneath it.
        count = 1
        for col in range(self.width):
            if count > self.width:
                break
            if col > 9:
                s += ' ' + str(col % 10)
                count += 1
            else:
                s += ' ' + str(col)
                count += 1
   
        return s

# 3.
    # the inputs
    def add_checker(self, checker, col):
        """ Adds the specific one-string checker to the proper column.
            """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker
        
# 4.
    # resetting the board
    def reset(self):
        """ Resets the Board object on which it is called by setting
            all slots to contain a space character.
            """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '

# 5.
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
            """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

# 6.
    # checking if a column is full
    def can_add_to(self, col):
        """ Returns True if it is valid to place a checker in the column col
            on the calling Board object. Otherwise, it should return False.
            """
        if col >= self.width or col < 0:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False

# 7.
    # checking if whole board is full
    def is_full(self):
        """ Returns True if the called Board object is completely full of checkers,
            and returns False otherwise.
            """
        count = True
        for col in range(self.width):
            if self.can_add_to(col) == True:
                count = False
            else:
                count = True
        return count

# 8.
    # removing a checker
    def remove_checker(self, col):
        """ Removes the top checker from column col of the called Board object.
            If the column is empty, then the method should do nothing.
            """
        assert(0 <= col < self.width)
        row = 0
        while self.slots[row][col] == ' ':
            row += 1
            if row >= self.height:
                row -= 1
                break
        self.slots[row][col] = ' '

# 9.

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ Returns True if there are four consecutive slots
            containing checker on the board. Otherwise, it should return False.
            """
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
