class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for ele in nums:
            idx = bisect.bisect_left(res, ele)
            if idx == len(res):
                res.append(ele)
            else:
                res[idx] = ele
        return len(res)