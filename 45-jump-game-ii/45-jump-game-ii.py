class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        jumps = 0
        far = 0
        for i in range(len(nums)-1):
            far = max(far, i+nums[i])
            if i == curr:
                curr = far
                jumps += 1
        return jumps