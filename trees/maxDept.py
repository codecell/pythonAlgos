# Q.) https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
'''
    Time complexity - since its recursive ~= O(n^2)
    Space complexity - O(1)
'''

def maxDepth(root):
    def recursive(node):
        if node is None:
            return 0

        leftCounter = recursive(node.left) + 1
        rightCounter = recursive(node.right) + 1

        return max(leftCounter, rightCounter)

    return recursive(root)

