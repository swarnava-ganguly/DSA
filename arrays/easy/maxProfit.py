# Leetcode:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Complexity: O(n)
# Intution:- keep finding the minimum in the array otherwise find max difference while iterating through out the array

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(0,len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit