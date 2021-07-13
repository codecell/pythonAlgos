# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# I'm basically just reverse - switching elems starting from the right k times, nums[-1] = nums[len(nums) - 1]
# nums[-2] = nums[len(nums) - 2]
#2) then switch the elements from size - k to size

def rotate(nums, k):
    numsSize = len(nums) - 1
    i = 0

    while i < k:
        nums[i], nums[i - k] = nums[i - k], nums[i]
        i += 1

    for j in range(numsSize - k, numsSize):
        nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

print(rotate([1,2,3,4,5,6,7], 3), '>>') # [5,6,7,1,2,3,4]   