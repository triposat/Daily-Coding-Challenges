class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, i, add, mini = 0, 0, 0, float("inf")
        while j < len(nums):
            add += nums[j]
            j += 1
            while add >= target:
                mini = min(mini, j-i)
                add -= nums[i]
                i += 1
        return mini if mini != float("inf") else 0