# Leetcode - https://leetcode.com/problems/rotate-array/description/
# Complexity - O(n)
# Optional Solution: reverse(nums, nums+k) => reverse(nums+k,len(nums)) => reverse(nums, nums+len(nums)) => O(2n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:] = nums[l-(k%l):] + nums[0:l-(k%l)]