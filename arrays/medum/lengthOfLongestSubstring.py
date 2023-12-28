# Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        hashset = set()
        maxlen = 0
        while r<len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                maxlen = max(maxlen,len(hashset))
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
        return maxlen
