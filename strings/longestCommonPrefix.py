# Q. https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

'''
    Space complexity - O(1)
    Time complexity - O(m * n) => length of the smallest string^2 in worst case
'''

def longestCommonPrefix(strs):
    smallest = min(strs, key=len)

    for indez in range(len(smallest)):
        for word in strs:
            if word[indez] != smallest[indez]:
                return smallest[0:indez]

    return smallest

print(longestCommonPrefix(['flower', 'flight', 'flow'])) # 'fl'
print(longestCommonPrefix(['glower', 'flight', 'flow'])) # ''
print(longestCommonPrefix(['lone', 'loner', 'lonely'])) # 'lone'