class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = -1
        num2 = -1
        n = len(nums)
        c1 = 0
        c2 = 0
        for i in range(n):
            if nums[i] == num1:
                c1 += 1
            elif nums[i] == num2:
                c2 += 1
            elif c1 == 0:
                num1 = nums[i]
                c1 = 1
            elif c2 == 0:
                num2 = nums[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = 0
        c2 = 0
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1
        res = []
        if c1 > n//3:
            res.append(num1)
        if c2 > n//3:
            res.append(num2)
        return res