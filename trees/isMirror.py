# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

'''
    time comlexity - O(n2)
    space - O(1)
'''

def isSymmetric(root):
    def inorderTrav(node, order):
        arr = []

        if node and order == 'left':
            arr += inorderTrav(node.left, 'left') + [node.val] + inorderTrav(node.right,'left')
        elif node and order == 'right':
            arr += inorderTrav(node.right, 'right') + [node.val] + inorderTrav(node.left, 'right')

        return  arr

    res1 = inorderTrav(root, 'left')
    res2 = inorderTrav(root, 'right')

    return res1 == res2