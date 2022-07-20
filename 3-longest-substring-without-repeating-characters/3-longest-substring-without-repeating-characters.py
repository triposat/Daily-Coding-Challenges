class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = -1
        hmap = {}
        ans = 0
        for i in range(n):
            if s[i] in hmap:
                left = max(left, hmap[s[i]])
            hmap[s[i]] = i
            ans = max(ans, i-left)
        return ans