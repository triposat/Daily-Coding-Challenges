class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        add = 0
        ans = 0
        hmap = {0: 1}
        for ele in nums:
            add += ele
            if add-k in hmap:
                ans += hmap[add-k]
            hmap[add] = hmap.get(add, 0)+1
        return ans