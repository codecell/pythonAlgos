# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

'''
    space complexity here is O(1)
    time is O(n)
'''
import re

def isPalindrome(s):
    # chars = ''.join(re.findall("[\w\d]", s.lower()))
    chars = [char.lower() for char in s if char.isalnum() ]

    i = 0
    j = len(chars) - 1

    while i <= j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False