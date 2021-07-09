# Que https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

'''
    Time complexity i think is O(n * m)
    space complexity = I am not sure,

    About my code, when I used same symbols to replace traversed index, I was getting results like [4, 9, '#'],
    So I decided to change the symbols for each of the arrays num1 and num2
'''

def intersectr(nums1, nums2):
    firstArrayLen = len(nums1)
    secArrayLen =  len(nums2)

    intersectionArr = []
    searcher = 0
    smallestLen = firstArrayLen

    if secArrayLen <= firstArrayLen:
        smallestLen = secArrayLen

    if firstArrayLen == smallestLen:
        while searcher < firstArrayLen:
            for loci in range(0, secArrayLen):
                if nums2[loci] == nums1[searcher]:
                    intersectionArr.append(nums1[searcher])
                    nums2[loci] = '#'
                    nums1[searcher] = '$'
            searcher += 1 
    else:
        while searcher < secArrayLen:
            for loci in range(0, firstArrayLen):
                if nums1[loci] == nums2[searcher]:
                    intersectionArr.append(nums2[searcher])
                    nums2[searcher] = '#'
                    nums1[loci] = '$'
            searcher += 1 

    return intersectionArr

a = [4, 9, 5]
b = [4, 6, 7, 9, 5]

print(intersectr(a, b))