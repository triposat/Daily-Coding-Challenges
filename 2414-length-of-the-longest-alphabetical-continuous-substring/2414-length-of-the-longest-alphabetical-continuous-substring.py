class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans=1
        cnt=1
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                cnt+=1
                ans=max(ans, cnt)
            else:
                cnt=1
        return ans