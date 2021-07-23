# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

'''
    Time complexity -- O(n)
    Space complexity -- O(1)
'''

import re

def strStr(haystack, needle):
    if needle == '':
        return 0

    macthObj = re.search(needle, haystack)

    if macthObj == None:
        return -1

    return macthObj.span()[0]


print(strStr("hello", 'll')) # 2
print(strStr("aaaaa", 'bba')) # -1
print(strStr("", 'a')) # -1
print(strStr("hello", '')) # 0
    