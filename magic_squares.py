"""
The below program is intended to:
1) Retrieve a positive, odd number from the user with which to create a magic square 
2) Create a magic square that is the user-specified number of rows by columns
3) Test that all rows, columns and diagonals do in fact add up to the same number

I have made use of numpy arrays for my grid

"""
import numpy as np

def validate_input(N):

    while True:
        
        if N == 1:
            N = int(input("1 is too small for a magic sqaure, enter a number that is 3 or greater:\n"))
        if N < 0:
            N = int(input("This is a negative number, please enter a positive integer:\n"))
        if N % 2 == 0:
            N = int(input("This is an even number. Please enter an odd integer:\n"))
        else:
            break
    
    return N

def create_square(odd_num):

    grid = np.zeros((odd_num, odd_num))

    i = 1
    # beginning in the middle of the first row
    r = 0
    c = odd_num // 2
    magic_total =  odd_num * (odd_num**2 + 1)/ 2

    # break loop when the grid is fully populated
    while i <= odd_num * odd_num:
        grid[r,c] = i
        i += 1
        # moving right diagonally upward
        r_next = (r - 1) % odd_num
        c_next = (c + 1) % odd_num
        # beginning again at the first column/last 
        # row if we leave the grid
        if grid[r_next, c_next]:
            r += 1
        # if the space is filled, move down instead
        else:
            r = r_next
            c = c_next

    print(f"A {odd_num}x{odd_num} magic square's rows, columns and diagonals should equate to {magic_total}.")
    print()
    return grid


def test_magic_square(odd_number, magic_square):

    # the below is the formula to ascertain the total
    # that each row/column/diagonal should be
    magic_total =  odd_number * (odd_number**2 + 1)/ 2
    # initialising a counter to count the number of times
    # our rows/columns/diagonals have met the criteria
    count = 0
    i = 0
    diagonal = 0

    while i < len(magic_square):
        sum_row = sum(magic_square[i,:])
        sum_col = sum(magic_square[:,i])
        sum_diagonal =  np.trace(magic_square)
        if sum_col == magic_total and sum_row == magic_total and sum_diagonal == magic_total:
            count += 1
        i += 1

    if count == odd_number:
        return f"All rows, columns and diagonals eqaute to {magic_total}. This is a magic square"
    else:
        return f"All rows, columns and diagonals do not equate to {magic_total}. This is not a magic square"
 
# in the below we call upon the methods that we have created

N = int(input("Please enter a positive, odd integer for which you would like a magic square created:\n"))
print()

valid_num = validate_input(N)

new_square = create_square(valid_num)
print(new_square)
print()
print(test_magic_square(valid_num, new_square))
