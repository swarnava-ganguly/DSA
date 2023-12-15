# Leecode:- https://leetcode.com/problems/two-sum/
# complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []

        for i in range(0,len(nums)):
            rem = target-nums[i]
            if rem in d and i != d[rem]:
                return [i,d[rem]]
            d[nums[i]] = i
        return []