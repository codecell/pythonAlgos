# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

def sortedArrayToBST(nums):
  # TreeNode(val)  => to instantiate a new Tree node

  def plant(arr):
    if arr is None:
      return

    mid_index = len(nums) // 2
    leftSide = arr[0:mid_index]
    rightSide = arr[mid_index + 1:]

    root = TreeNode(arr[mid_index]) # root node

    root.left = plant(leftSide)
    root.right = plant(rightSide)

    return root

  return plant(nums)
