# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

'''
    Runtime - O(n)
    space complexity - O(1)
'''

from collections import defaultdict
def firstUniqChar(s):
    d = defaultdict(int)

    for char in s:
        d[char] += 1
    
    for x in d:
        if d[x] == 1:
            return s.index(x)
    
    return -1

print(firstUniqChar('leetcode'))
print(firstUniqChar('aabb'))
print(firstUniqChar('x'))