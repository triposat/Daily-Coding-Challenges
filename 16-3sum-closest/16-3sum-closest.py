class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        nums.sort()
        closest = float("inf")
        for i in range(nums_len - 2):
            left, right = i + 1, nums_len - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum) < abs(target - closest):
                    closest = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest