class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x: (-x[0], x[1]))
        ans, cur = 0, 0
        for a, d in p:
            if d < cur:
                ans += 1
            else:
                cur = d
        return ans