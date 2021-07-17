# Q.https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
'''
    So I basically map each row and each column of the sudoku board
    to 2 dictionaries respecticvely and check if any of the values[1 t0 9] appears more than once in any row or column.
'''

from collections import defaultdict


def isValidSudoku(board):
    size = len(board)
    i = 0
    j = 0

    while i < size and j < size:
        for k in range(0, size):
            rows = defaultdict(int)
            cols = defaultdict(int)
            for l in range(0, size):
                if board[k][l] != ".":
                    rows[board[k][l]] += 1 #rows

                if board[l][k] != ".":
                    cols[board[l][k]] += 1 #vertically
            
            
            for y in rows:
                if rows[y] > 1:
                    return False
            
            for x in cols:
                if cols[x] > 1:
                    return False
        i += 1
        j += 1
    
    return True

boardOne = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

secondBoard = [
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(boardOne)) #true
print(isValidSudoku(secondBoard)) #False