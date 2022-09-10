class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        add, ans = 0, 0
        for ele in nums:
            add += ele
            if add-k in seen:
                ans += seen[add-k]
            seen[add] = seen.get(add, 0)+1
        return ans