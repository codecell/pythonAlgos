# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# I'm basically just reverse - switching(swapping) elems starting from the right k times, nums[-1] = nums[len(nums) - 1]
# nums[-2] = nums[len(nums) - 2]
#2) solution 2 build on the fact that after rotation, new position of an item corresponds to (index + k) % lengthOfList, 
# space complexity tho increases by 1

def rotate(nums, k):
    res = []
    size = len(nums)

    for i in range(0, size):
        newPositionInRes = (i + k) % size
        # res[newPositionInRes] = nums[i] indexError
        res.insert(newPositionInRes, nums[i])

    for i in range(0, size):
        # update nums with rotated indexes
        nums[i] = res[i]

    return nums

print(rotate([1,2,3,4,5,6,7], 3), '>>') # [5,6,7,1,2,3,4]   

# solution 1
# numsSize = len(nums)
# i = 0

# while i < k:
#     for j in range(0, numsSize):
#         nums[j], nums[numsSize - 1] = nums[numsSize - 1], nums[j]

#     i += 1