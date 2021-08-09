# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

'''
    Time complexity - O(m + n + k) ~= O(3n) ~= O(n)
    Space complexity - O(1)
'''
def mergeTwoLists(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    merged = ListNode(0)
    tracer = merged

    while l1 is not None and l2 is not None:
        firstVal = l1.val
        secVal = l2.val

        if firstVal <= secVal:
            tracer.next = l1
            l1 = l1.next
        else:
            tracer.next = l2
            l2 = l2.next

        tracer = tracer.next

    if l1 == None:
        tracer.next = l2
    
    if l2 == None:
        tracer.next = l1

    return merged.next