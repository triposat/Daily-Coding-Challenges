class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('inf')
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                add=nums[i]+nums[l]+nums[r]
                if abs(add-target)<abs(ans-target):
                    ans=add
                if add<target:
                    l+=1
                elif add>target:
                    r-=1
                else:
                    return add
        return ans
    
