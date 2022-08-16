class Solution:
    def firstUniqChar(self, s: str) -> int:
        hey=Counter(s)
        # print(hey)
        for idx, val in enumerate(s):
            if val in hey and hey[val]==1:
                return idx
        return -1