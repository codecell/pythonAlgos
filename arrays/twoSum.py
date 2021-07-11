# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

''' 
    for solution 2
    time complexity here is O(n * n) in the worst case
    The Space complexity is constant here since the whole operation is modified in place and no new arrays are created O(1) 
'''

from collections import defaultdict

def twoSum(nums, target):

    d = defaultdict(int)

    # hash the values of nums to their index as keys of the hash table 
    # in the same lookup check the table again to see if an already hashed index complements the current 
    # item of nums before hashing it
    # space complexity here is O(m), time complexity is less than O(n * n) { I think } since lookup time in a hash table 
    # is constant

    for indez in range(0, len(nums)):
        d[indez] = nums[indez]
        complement = target - nums[indez]

        for key in d:
            if d[key] == complement and key != indez:
                return [indez, key]

    ''' solution 2
    currentIndez = 0

    lent = len(nums)

    while currentIndez < lent:
        for k in range(currentIndez + 1, lent):
            if nums[currentIndez] + nums[k] == target and currentIndez != k:
                return [currentIndez, k]
    '''

print(twoSum([2, 2, 6, 1, 3], 5))