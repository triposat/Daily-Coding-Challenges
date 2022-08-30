class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # pref=[0]*(len(nums)+1)
        for i in range(1, len(nums)):
            # pref[i+1]=pref[i]+num
            nums[i]=nums[i-1]+nums[i]
        return [bisect_right(nums, q) for q in queries]