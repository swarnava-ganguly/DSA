# Leetcode:- https://leetcode.com/problems/majority-element/description/
# Complexitu: O(n)
# Space Complexity: O(1)
# Algorithm Name: Moore's Voting Algorithm
# Intution:- if some element appear more than N/2 times, it will not get cancelled out. This algorithm is saving space
# Other Algorithm: 2 loops is brute force one, using hashing we can solve it with linear time complexity but also with linear space Complexity.

# Key Note:- Majority element is defined when there is a element which is greater than N/2. Then only the above algo will work. Otherwise there is no majority element in the array. You can check it by running through the entire loop with additional O(n).
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(0,len(nums)):
            if cnt == 0:
                element = nums[i]
                cnt = 1
            elif nums[i] == element:
                cnt += 1
            else:
                cnt -= 1
        # to check if there is any element whose occourance is greater than n//2
        # cnt = 0
        # for i in nums:
        #     if i == element:
        #         cnt += 1
        # if cnt < len(nums)//2:
        #     return -1
        return element