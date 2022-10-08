class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            l = i+1
            r = n-1
            temp = -1*nums[i]
            while l < r:
                add = nums[l]+nums[r]
                if add < temp:
                    l += 1
                elif add > temp:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return ans