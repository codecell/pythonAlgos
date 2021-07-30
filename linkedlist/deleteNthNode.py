# Q.) https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

def removeNthFromEnd(head, n: int):
    holderList = ListNode()
    holderList.next = head
    tracer = head
    lent = 0

    # To get the length
    while tracer != None:
        tracer = tracer.next

        lent += 1

    lent -= n
    tracer = holderList

    while lent > 0:
        tracer = tracer.next

        lent -= 1
    
    tracer.next = tracer.next.next

    return holderList.next


