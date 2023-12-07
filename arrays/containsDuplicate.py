# Leetcode - https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dect = {}
        for i in nums:
          if i in dect.keys() and dect[i] >= 1:
             return True
          else:
             dect[i] = dect.get(i,0) + 1
        return False