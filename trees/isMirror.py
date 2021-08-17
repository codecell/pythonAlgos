# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

'''
    time comlexity - O(n^2)
    space - O(1)
'''

def isSymmetric(root):

    def trav(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False

        if not trav(left.left, right.right):
            return False
        if not trav(left.right, right.left):
            return False
        
        return True

    return isSymmetric(root.left, root.right)