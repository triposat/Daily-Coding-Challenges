class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum3 = nums[i]  + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                    
                if sum3 < target:
                    l += 1

                elif sum3 > target:
                    r -= 1

                else:
                    return sum3

        return ans