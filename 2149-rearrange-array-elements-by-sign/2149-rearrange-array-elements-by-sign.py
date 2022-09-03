class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)
        pos, neg = 0, 1
        for ele in nums:
            if ele > 0:
                ans[pos] = ele
                pos += 2
            else:
                ans[neg] = ele
                neg += 2
        return ans