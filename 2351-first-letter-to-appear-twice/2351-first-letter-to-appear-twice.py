class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hset = set()
        for ele in s:
            if ele in hset:
                return ele
            else:
                hset.add(ele)