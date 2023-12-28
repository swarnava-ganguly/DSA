# Leetcode:- https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# Time Complexity:- O(n)
# Space Complexity:- O(n)
# Intution:-  the bellow code will only work if the number of positive and negitives are equall

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        l = [0]*len(nums)
        for i in nums:
            if i > 0:
                l[pos] = i
                pos += 2
            else:
                l[neg] = i 
                neg += 2
        return l

# Intution:-  if the number of positives and negitives are not equall, then the beloow code will work
# Time Complexity:- O(2N)
# Space Complexity:- O(N)

def alternateNumbers(a : List[int]) -> List[int]:
    neg = []
    pos = []
    for i in a:
        if i>0:
            pos.append(i)
        else:
            neg.append(i)
    if len(pos) > len(neg):
        for i in range(0,len(neg)):
            a[2*i] = pos[i]
            a[2*i+1] = neg[i]
        for i in range(2*len(neg), len(pos)):
            a[i] = pos[i]
    else:
        for i in range(0,len(pos)):
            a[2*i] = pos[i]
            a[2*i+1] = neg[i]
        for i in range(2*len(pos), len(neg)):
            a[i] = neg[i]
    return a