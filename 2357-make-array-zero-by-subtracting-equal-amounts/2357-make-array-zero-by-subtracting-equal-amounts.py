class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for ele in nums:
            if ele != 0:
                s.add(ele)
        return len(s)
