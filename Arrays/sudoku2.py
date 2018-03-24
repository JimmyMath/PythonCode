#Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

#Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

#Example

#For

#grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

#the output should be
#sudoku2(grid) = true;

#For

#grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

#the output should be
#sudoku2(grid) = false.

#The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.array.char grid

#A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

#[output] boolean

#Return true if grid represents a valid Sudoku puzzle, otherwise return false.

import numpy as np
from collections import Counter
import itertools
def sudoku2(grid):
    
    grid=np.array(grid)
    
    for i in range(0,9):
        c=Counter(grid[i,:])
        for z in grid[i,:]:
            if c[z]>1 and z!='.':
                    return False
    
    for j in range(0,9):
        c=Counter(grid[:,j])
        for y in grid[:,j]:
            if c[y]>1 and y!='.':
                    return False
                
    for h,k in itertools.product([1,4,7],[1,4,7]):
        sub=[]
        for a,b in itertools.product([-1,0,1],[-1,0,1]):
            sub.append(grid[h+a][k+b])
        c=Counter(sub)
        for w in sub:
            if c[w]>1 and w!='.':
                return False
    
    return True
