# Coding Ninja: https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_5713505?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# prefix sum
# optimal for zeros and negitive O(NlogN)
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    sum=0
    d = {}
    maxlen=0
    for i in range(0,len(nums)):
        sum = sum+nums[i]
        rem = sum - k
        if sum == k:
            maxlen = max(maxlen,i+1)
        if rem in d:
            len1 = i - d[rem]
            maxlen = max(maxlen,len1)
        if sum not in d:
            d[sum] = i
    return maxlen

# Coding Ninja:- https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# 2 pointer
# optimal for positive 0(2N)
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    lp = 0
    rp = 0
    maxlen = 0
    sum = a[0]
    while rp < len(a):
        while sum > k and lp <= rp:
            sum = sum - a[lp]
            lp += 1
        if sum == k:
            maxlen = max(maxlen,rp-lp+1)
        rp += 1
        if rp < len(a):
            sum = sum + a[rp]
        
    return maxlen
