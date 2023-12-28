# Leetcode - https://leetcode.com/problems/max-consecutive-ones/description/
# Complexity - O(n)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for i in nums:
            if i==1:
                count += 1
            else:
                maximum = max(maximum,count)
                count = 0
        maximum = max(maximum,count)
        return maximum