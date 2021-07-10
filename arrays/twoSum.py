# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

'''
    time complexity here is O(n * n) in the worst case
    The Space complexity is constant here since the whole operation is modified in place and no new arrays are created O(1) 
'''

def twoSum(nums, target):
    currentIndez = 0

    lent = len(nums)

    while currentIndez < lent:
        for k in range(currentIndez + 1, lent):
            if nums[currentIndez] + nums[k] == target and currentIndez != k:
                return [currentIndez, k]


print(twoSum([2, 2, 6, 1, 3], 5))