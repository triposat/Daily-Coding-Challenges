class Solution:
    def dfs(self, start, k, n, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
            return
        for i in range(start, 10):
            self.dfs(i+1, k-1, n-i, path+[i], res)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(1, k, n, [], res)
        return res