class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        binAr = sorted(bin(num).count('1') for num in set(nums))
        i = 0
        j = len(binAr)-1
        ans = 0
        while i < j:
            if binAr[i]+binAr[j] >= k:
                ans += (j-i)*2  # Pair could be (1, 2) or (2, 1)
                j -= 1
            else:
                i += 1
        for num in binAr:
            if num*2 >= k:
                ans += 1
        return ans