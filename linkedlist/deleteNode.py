# Q). https://leetcode.com/submissions/detail/529594058/?from=explore&item_id=553

'''
    Time complexity -- O(n)
    Space Complexity -- O(1)
'''

def deleteNode(self, node):
    temp = node.next
    node.val = temp.val

    node.next = node.next.next


print(deleteNode([4, 5, 1, 9], 5)) #[4, 1, 9]
print(deleteNode([-3, 1, -9], -3)) #[1, -9]