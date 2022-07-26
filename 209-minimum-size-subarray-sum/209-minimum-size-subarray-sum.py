class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def bSear(left, right, val):
            while left < right:
                mid = (left+right) >> 1
                if val-nums[mid] >= target:
                    left = mid+1
                else:
                    right = mid
            return left
        res = len(nums)+1
        for idx, val in enumerate(nums[1:], 1):
            nums[idx] = nums[idx-1]+val
        left = 0
        for right, val in enumerate(nums):
            if val >= target:
                left = bSear(left, right, val)
                res = min(res, right-left+1)
        return res if res <= len(nums) else 0