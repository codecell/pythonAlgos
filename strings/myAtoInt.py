# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
    '''
        space complexity O(n)
        time complexity O(n)

        Regex explanation =>
        ^       --starts with
        \s*     --with zero or more spaces
        [-|+]?  --with or without a +ve or -ve sign
        \d+     --one or more digits
    '''

import re

def myAtoi(s):
    numsList = re.findall('^\s*[-|+]?\d+', s)
    numString = ''.join(numsList)
    
    if numsList == []:
        return 0
    
    if int(numString) < -1 * 2**31:
        return -1 * 2**31
    
    if int(numString) > 2**31 - 1:
        return 2**31 - 1
    
    return int(numString)


print(myAtoi('42')) # 42
print(myAtoi(' -42')) # -42
print(myAtoi('42 with words')) # 42
print(myAtoi('words at beginning 4254')) # 0
