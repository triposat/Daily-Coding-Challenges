class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        ans = set()
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] in ans:
                return True
            ans.add(nums[i]+nums[i+1])
        return False
