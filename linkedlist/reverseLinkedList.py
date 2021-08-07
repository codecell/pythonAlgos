# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

'''
    Time complxity - O(n)
    Space complexity - O(1)
'''

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
        # head = prev
        
    # print(head)
    return prev

print(reverseList([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverseList([9, 8])) # [8, 9]