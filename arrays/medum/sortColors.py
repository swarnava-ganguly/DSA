# Leetcode:- https://leetcode.com/problems/sort-colors/description/
# Complexity: O(n)
# Best Algo: Dutch National Flag Algorithm
# Brute Force Algo: sorting
# Better Algo: count the number of 0,1,2 and create a array accordingly



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
        