class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        add = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                res = max(res, add)
                add = 0
            add += nums[i]
        return max(add, res)