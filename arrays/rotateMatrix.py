# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

'''
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ==> Rotate 90 degrees
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    so basically each element is moved(swapped) from index to index + 2,

'''

def rotate(matrix):
    size = len(matrix)

    for row in range(0, size // 2): # current index
        for col in range(row, size - 1 - row): # An item 2 indexes ahead
            matrix[row][col], matrix[col][size - 1 - row] = matrix[col][size - 1 - row], matrix[row][col] # 0,0 and 0,2
            matrix[row][col], matrix[size - 1 - row][size - 1 - col] = matrix[size - 1 - row][size - 1 - col], matrix[row][col]
            # Line above, first swap moves m[0][2] to m[0][0] so swap m[0][0] with m[2][2]
            matrix[row][col], matrix[size - 1 - col][row] = matrix[size - 1 - col][row], matrix[row][col]
            # Second swap also moves item that was at m[2][2] to m[0][0], last swap finally corrects it by swapping 
            # that at m[0][0] with m[2][0]
    
    return matrix



print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  #[[7, 4, 1], [8, 5, 2], [9, 6, 3]]