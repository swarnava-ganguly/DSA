# Leetcode:- https://leetcode.com/problems/maximum-subarray/
# Complexity:- O(n)
# Space Complexity: O(1)
# Algorithm: kadane's Algorithm
# Intution:- This problem states that you need to find the max summation of subarray. Not logest subarray to match kth sum. In that case we must use prefix sum or two pointer(if all positive)
#            So logic is like do the sum of all numbers in the array and store the max of sum value in a variable. If sum is less than zero, reset the value of some to 0\

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        sum = 0
        for num in nums:
            sum = sum + num
            if sum < 0:
                sum = 0
            maxi = max(maxi,sum)
        return maxi