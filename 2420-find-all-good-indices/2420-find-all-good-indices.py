class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pre = [1]*(n+1)
        post = [1]*(n+1)
        res = []
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                pre[i] = pre[i-1]+1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                post[i] = post[i+1]+1
        for i in range(k, n-k):
            if pre[i-1] >= k and post[i+1] >= k:
                res += [i]
        return res