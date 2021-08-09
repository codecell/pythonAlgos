# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

def isPalindrome(head):
    current = head
    arr = []
        
    while current is not None:
        arr.append(current.va)
        current = current.next

    return arr[::-1] == arr

print(isPalindrome([1, 2, 2, 1])) # true
print(isPalindrome([1, 2, 2, 4])) # false