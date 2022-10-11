class Solution:
    def goodDaysToRobBank(self, s: List[int], time: int) -> List[int]:
        n = len(s)
        pre = [0]*(n+1)
        post = [0]*(n+1)

        for i in range(1, n):
            if s[i] <= s[i-1]:
                pre[i] = pre[i-1]+1

        for i in range(n-2, -1, -1):
            if s[i] <= s[i+1]:
                post[i] = post[i+1]+1

        ans = []
        print(pre, post)
        for i in range(time, n-time):
            if pre[i] >= time and post[i] >= time:
                ans += [i]
        return ans