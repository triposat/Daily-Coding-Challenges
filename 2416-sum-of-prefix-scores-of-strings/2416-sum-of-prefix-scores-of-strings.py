class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hmap = defaultdict(int)
        for w in words:
            for i in range(len(w)):
                hmap[w[:i+1]] += 1
        res = []
        for w in words:
            ans = 0
            for i in range(len(w)):
                ans += hmap[w[:i+1]]
            res.append(ans)
        return res