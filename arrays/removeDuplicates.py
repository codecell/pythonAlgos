# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    i = len(nums) - 1

    if len(nums) == 1:
        return len(nums)

    while i >= 0:
        if nums[i] == nums[i - 1] and i - 1 >= 0:
            # i - 1 >= 0 is meant to handle case whereby i - 1 is negative because nums[-1] == nums[len(nums) - 1]    
            del nums[i] 
            # delete d duplicate from the end of the array
        i -= 1

    return len(nums)

# print(removeDuplicates([0, 0, 1, 2, 2, 3, 3, 3, 4]))

arr = [3, 5, 5]
print(arr.index(max(arr)), '<< >>')