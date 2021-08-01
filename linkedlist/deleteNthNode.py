# Q.) https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

def removeNthFromEnd(head, n: int):
    holderList = head
    lent = 1

    # To get the length
    while head.next:
        head = head.next

        lent += 1

    head = holderList

    if n == lent:
        return holderList.next

    iterations = lent - n - 1

    for i in range(iterations):
        head = head.next

    head.next = head.next.next

    return holderList


