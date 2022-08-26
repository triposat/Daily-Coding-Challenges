class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        total = sum(nums)
        maxS = -float("inf")
        minS = float("inf")
        for ele in nums:
            sum1 += ele
            maxS = max(maxS, sum1)
            if sum1 < 0:
                sum1 = 0

            sum2 += ele
            minS = min(minS, sum2)
            if sum2 > 0:
                sum2 = 0

        return maxS if total == minS else max(maxS, total-minS)
