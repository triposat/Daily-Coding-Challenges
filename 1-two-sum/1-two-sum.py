class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, val in enumerate(nums):
            rem = target-val
            if rem in hmap:
                return [hmap[rem], idx]
            hmap[val] = idx
