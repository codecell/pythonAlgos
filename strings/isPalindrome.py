# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
import re

def isPalindrome(s):
    chars = ''.join(re.findall("[\w\d]", s.lower()))

    i = 0
    j = len(chars) - 1

    while i <= j:
        if chars[i] != chars[j] and chars[j] != '_' and chars[i] != '_':
            return False
        i += 1
        j -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False