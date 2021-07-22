# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

import string

def myAtoi(s):
    st = s.translate(str.maketrans('', '', string.whitespace))
    lent = len(st)
    numStr = ''

    for i in range(0, lent):
        if lent > i + 1 and st[i].isalpha() == True and st[i + 1].isalpha() == False:
            return 0
        if st[i].isalpha() == False:
            numStr += st[i]

    if int(numStr) < (-1 * (2**31)):
        return (-1 * (2**31))
    elif int(numStr) > 2**31 - 1:
        return 2**31 - 1
    
    return int(numStr)


print(myAtoi('42')) # 42
print(myAtoi(' -42')) # -42
print(myAtoi('42 with words')) # 42
print(myAtoi('words at beginning 4254')) # 0
