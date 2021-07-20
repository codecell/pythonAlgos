# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
'''
    Time complexity - O(n + m)
    Space complexity - O(1)
'''
from collections import defaultdict

def isAnagram(s, t):
    ds = defaultdict(int)
    dt = defaultdict(int)

    for y in s:
        ds[y] += 1
    
    for x in t:
        dt[x] += 1

    return ds == dt   
    
    # solution 1
    # return sorted(s) == sorted(t)

print(isAnagram('anagram', 'nagaram')) #true
print(isAnagram('car', 'cat')) #false
