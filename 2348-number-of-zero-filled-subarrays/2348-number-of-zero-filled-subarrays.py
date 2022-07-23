class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for ele in nums:
            if ele != 0:
                ans += (cnt*(cnt+1)//2)
                cnt = 0
            else:
                cnt += 1
        ans += (cnt*(cnt+1)//2)
        return ans