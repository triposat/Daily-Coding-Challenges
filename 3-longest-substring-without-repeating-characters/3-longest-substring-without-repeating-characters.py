class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a c b d b a c d
        st=0
        seen={}
        ans=0
        for end in range(len(s)):
            if s[end] not in seen:
                ans=max(ans, end-st+1)
            else:
                if seen[s[end]]>=st:
                    st=seen[s[end]]+1
                else:
                    ans=max(ans, end-st+1)
            seen[s[end]]=end
        return ans