# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
import re

def isPalindrome(s):
    chars = ''.join(re.findall("[a-zA-z\d]", s.lower()))

    reversedStr = ''

    for ch in chars:
        reversedStr = ch + reversedStr

    return reversedStr == chars


print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False