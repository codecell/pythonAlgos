# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

'''
    time complexity --- O(n)
    space -- O(m)
'''

def plusone(digits):
    res = []

    arrToStr = ''.join(str(el) for el in digits)
    arrToStrToInt = int(arrToStr) + 1

    intToStr = str(arrToStrToInt)
    
    for item in intToStr:
        res.append(int(item))

    return res


print(plusone([9])) #[1, 0]
print(plusone([1, 2, 3])) #[1, 2, 3]
