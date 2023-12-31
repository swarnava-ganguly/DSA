# Leetcode: https://leetcode.com/problems/longest-palindrome/description/?source=submission-ac
# Complexity: O(n)
# Space Complexity: O(n)
# Intitution:
#   Create Frequency for each character 
#   Even number of characters can be taken as it is as these can be partition in 2 halves. 
#   For odd number of characters take n-1 characters and add 1 at the end if we encounter any odd character 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for char in s:
            d[char] = d.get(char,0)+1
        reslen = 0
        for key in d:
            if d[key] % 2 == 0:
                reslen = reslen + d[key]
            else:
                isOdd = True
                reslen = reslen +d[key] - 1
        return reslen if len(s)==reslen else reslen+1