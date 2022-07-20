class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        ans = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == prev+1:
                cur += 1
            elif nums[i] != prev:
                cur = 1
            prev = nums[i]
            ans = max(ans, cur)
        return ans