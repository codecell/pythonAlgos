# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

'''
    Runtime - O(n)
    Space Complexity - O(1)
'''
def hasCycle(head):
    if head == None or head.next == None:
        # means there was a termination
        return False

    slowPointer, fastPointer = head, head.next

    while slowPointer != fastPointer:
        if fastPointer == None or fastPointer.next == None:
            # fastPointer or fastPointer.next will eventually == None if no cycle
            return False

        slowPointer, fastPointer = slowPointer.next, fastPointer.next.next

    # if it gets here then, fastPointer == fastPointer.next == a point in cycle == loop

    return True