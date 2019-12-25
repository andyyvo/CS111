#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

# option 2

def mult_row(matrix, r, m):
    """ multiplies row 'r' of the specified matrix by the specified multiplier 'm'
    """
    for x in range(len(matrix)):
        if x == r:
            for i in range(len(matrix[0])):
                matrix[x][i] *= m

# option 3

def add_row_into(matrix, source, dest):
    """ adds each element of the row with index 'source' (source row)
        to the corresponding element of the row with index 'dest' (destination row)
        of the specified 2-D list 'matrix'
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r == source:
                matrix[dest][c] += matrix[source][c]

# option 4

def add_mult_row_into(matrix, m, source, dest):
    """ takes the specified 2-D list 'matrix' and
        adds each element of row 'source' (source row),
        multiplied by 'm' to the corresponding element
        row 'dest' (destination row)
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r == source:
                matrix[dest][c] += (m * matrix[source][c])

# option 5

def create_matrix(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    matrix1 = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        matrix1 += [row]

    return matrix1

def transpose(matrix):
    """ the transpose of an 'n x m' matrix is a new 'm x n' matrix
        in which the rows of the original matrix become the
        columns of the new one, and vice versa.

        creates and returns a new 2-D list that is the transpose
        of 'matrix'.
        original 2-D list is not changed.
    """
    width = len(matrix)
    height = len(matrix[0])
    newmatrix = create_matrix(height, width)
    for r in range(height):
        for c in range(width):
            newmatrix[r][c] = matrix[c][r]
    return newmatrix

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here

        elif choice == 2:
            r = int(input('Index of row: '))
            m = float(input('Multiplier: '))
            mult_row(matrix, r, m)
        elif choice == 3:
            source = int(input('Index of source row: '))
            dest = int(input('Index of destination row: '))
            add_row_into(matrix, source, dest)
        elif choice == 4:
            source = int(input('Index of source row: '))
            dest = int(input('Index of destination row: '))
            m = float(input('Multiplier: '))
            add_mult_row_into(matrix, m, source, dest)
        elif choice == 5:
            matrix = transpose(matrix)
            matrix
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
