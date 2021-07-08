# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

def containsDuplicate(nums): 
    if len(nums) <= 1:
        return False

    i = 0
    k = len(nums) - 1

    while i + 1 <= k:
        if nums[i] == nums[k]:
            return True

        i += 1
        k -= 1

    return False    

print(containsDuplicate([1, 2, 3, 4]))