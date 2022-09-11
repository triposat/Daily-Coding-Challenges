class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if not num & 1:
                hmap[num] = hmap.get(num, 0)+1

        if not hmap:
            return -1

        ans = (1 << 31)
        t = 1
        for key, val in hmap.items():
            if val > t or val == t and key < ans:
                ans = key
                t = val
        return ans
