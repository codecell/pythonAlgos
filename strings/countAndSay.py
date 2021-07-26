# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/


def countAndSay(n):
    if n == 1: return '1'
    
    outStr = '1'
    i = 2
    while i <= n:
        count = 1
        holder = []
        prev = outStr[0]

        for j in range(1, len(outStr)):
            if outStr[j] != prev:
                holder.append(str(count) + outStr[j - 1])
                count = 0
            count += 1
            prev = outStr[j]
        holder.append(str(count) + outStr[-1])
        outStr = ''.join(holder)
        i += 1
    return outStr
print(countAndSay(1)) # '1'
print(countAndSay(2)) # '11'
print(countAndSay(3)) # '21'
print(countAndSay(4)) # '1211'
print(countAndSay(5)) # '111221'
print(countAndSay(6)) # '312211'
print(countAndSay(7)) # '13112221'

