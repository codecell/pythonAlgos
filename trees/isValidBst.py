# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625

def isValidBST(root):

    def traverse(node):
        arr = []

        if node:
            arr.append(traverse(node.left) + [node.val] + traverse(node.right))

        return arr

    result = traverse(root) # sorted List after in-order traversal

    for i in range(1, len(result)):
        if result[i - 1] >= result[i]:
            return False

    return True