class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                n2 += 1
                nums[n2] = 2
                n1 += 1
                nums[n1] = 1
                n0 += 1
                nums[n0] = 0
            elif nums[i] == 1:
                n2 += 1
                nums[n2] = 2
                n1 += 1
                nums[n1] = 1
            elif nums[i] == 2:
                n2 += 1
                nums[n2] = 2