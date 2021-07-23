# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

'''
    Time complexity -- O(n)
    Space complexity -- O(1)
'''

import re

def strStr(haystack, needle):
    if needle == '':
        return 0

    macthSpan = re.search(needle, haystack)

    if macthSpan == None:
        return -1

    return macthSpan.span()[0]


print(strStr("hello", 'll')) # 2
print(strStr("aaaaa", 'bba')) # -1
print(strStr("", 'a')) # -1
print(strStr("hello", '')) # 0
    