class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 10 22 42 33 21 50 41 60 80 3
        res = []
        hmap = defaultdict(list)
        for num in nums:
            idx = bisect_left(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num
            hmap[idx].append(
                (sum(l if ele < num else 0 for l, ele in hmap[idx-1]) or 1, num))
        return sum(l for l, ele in hmap[len(res)-1])