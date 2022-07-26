# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         def bSear(left, right, val):
#             while left < right:
#                 mid = (left+right) >> 1
#                 if val-nums[mid] >= target:
#                     left = mid+1
#                 else:
#                     right = mid
#             return left
#         res = len(nums)+1
#         nums = [sum(nums[0:i:1]) for i in range(len(nums)+1)][1:]
#         for right, val in enumerate(nums):
#             left=0
#             if val >= target:
#                 left = bSear(left, right, val)
#                 res = min(res, right-left+1)
#         return res if res <= len(nums) else 0
class Solution:

    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left