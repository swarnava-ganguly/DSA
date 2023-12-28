# Leetcode:- https://leetcode.com/problems/maximum-subarray/
# Complexity:- O(n)
# Space Complexity: O(1)
# Algorithm: kadane's Algorithm
# Intution:- This problem states that you need to find the max summation of subarray. Not logest subarray to match kth sum. In that case we must use prefix sum or two pointer(if all positive)
#            So logic is like do the sum of all numbers in the array and store the max of sum value in a variable. If sum is less than zero, reset the value of some to 0\

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = nums[0]
        for i in range(0,len(nums)):
            sum = sum +nums[i]
            maxsum = max(maxsum,sum)
            if sum < 0:
                sum = 0
        return maxsum