# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n=len(nums)
#         last=n-1
#         for i in range(n-2, -1, -1):
#             if i+nums[i]>=last:
#                 last=i
#         return True if last==0 else False
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        jumps = 0
        far = 0
        for i in range(len(nums)-1):
            far = max(far, i+nums[i])
            if i == curr:
                curr = far
                jumps += 1
            if i >= far:
                return False
        return True