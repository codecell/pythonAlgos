# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

def reverse(x):
    numToStr = str(abs(x))

    revd = ''

    for i in range(len(numToStr) -1, -1, -1):
        revd = revd + numToStr[i]

    if int(revd) > 2**31 - 1:
        return 0
    
    if x < 0:
        return -1 * int(revd)
    
    return 1 * int(revd)

print(reverse(123)) # 321
print(reverse(-56723)) #-32765
print(reverse(1234567898)) # 0