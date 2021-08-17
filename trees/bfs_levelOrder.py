# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628
'''
  time - O(n)
  space - O(n)
'''
def levelOrder(root):
  h = defaultdict(int)

  def addLevel(node, level):
    if node:
      level += 1
      addLevel(node.left, level)
      addLevel(node.right, level)

      if h[level]:
        h[level].append(node.val) #{1: [val]}
      else:
        h[level] = [node.val]

  addLevel(root, 0)
  res = []

  for i in range(1, len(h.keys()) + 1):
    res.append(h[i])

  return res