class Solution:
    def twoSum(self, arr: List[int], k: int) -> List[int]:
        from collections import defaultdict
        s = defaultdict(int)
        cnt = 0
        for idx, ele in enumerate(arr):
            if k-ele in s:
                return [s[k-ele], idx]
            s[ele] = idx
        return cnt
