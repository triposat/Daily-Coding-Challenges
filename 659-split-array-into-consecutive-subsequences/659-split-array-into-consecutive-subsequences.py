class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        hmap = Counter(nums)
        seq = []
        for num in sorted(hmap.keys()):
            count = hmap[num]
            n = len(seq)-1
            for _ in range(count):
                if n >= 0 and seq[n][-1]+1 == num:
                    seq[n].append(num)
                    n -= 1
                else:
                    seq.append([num])
        for s in seq:
            if len(s) < 3:
                return False
        return True