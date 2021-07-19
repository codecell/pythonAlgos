# Q) https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
'''
    space complexity => O(1)
    time complexity O(n)

    for e.g ['h', 'e', 'l', 'l', 'o,] => ['o', 'l', 'l', 'e', 'h']
    each item eventually takes d position from i to len - i - 1, this should take n/2 iterations to swap, 
    to cover for when len(n) is an odd number, we do n//2 + n % 2 iterations
'''

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    lent = len(s)
    
    for indez in range(0, (lent // 2) + lent % 2):
        s[lent - 1 - indez], s[indez] = s[indez], s[lent - 1 - indez]

    # Return here is just for testing the solution, swap is done in-place as instructed
    return s
    


print(reverseString(['h', 'e', 'l', 'l', 'o'])) #['o', 'l', 'l', 'e', 'h']
print(reverseString(['1', '2', '3', '4', '5', '6'])) #['6', '5', '4', '3', '2', '1']