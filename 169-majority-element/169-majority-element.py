class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if cnt == 0:
                candi = num
            if candi == num:
                cnt += 1
            else:
                cnt -= 1
        return candi