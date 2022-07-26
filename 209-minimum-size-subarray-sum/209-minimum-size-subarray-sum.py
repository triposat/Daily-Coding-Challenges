class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        i=0
        add=0
        mini=float("inf")
        while j<len(nums):
            add+=nums[j]
            j+=1
            while add>=target:
                mini = min(mini, j-i)
                add-=nums[i]
                i+=1
        return mini if mini!=float("inf") else 0