class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)
        return ans


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)