class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        temp = nums[0]
        st = 0
        ans = 0
        for end in range(len(nums)):
            while st < end and temp & nums[end]:
                temp ^= nums[st]
                st += 1

            temp |= nums[end]
            ans = max(ans, end-st+1)
        return ans