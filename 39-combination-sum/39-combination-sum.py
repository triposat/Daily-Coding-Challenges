class Solution:
    def dfs(self, arr, tar, idx, path, res):
        if tar < 0:
            return
        if tar == 0:
            res.append(path)
            return
        for i in range(idx, len(arr)):
            self.dfs(arr, tar-arr[i], i, path+[arr[i]], res)

    def combinationSum(self, arr: List[int], tar: int) -> List[List[int]]:
        res = []
        arr.sort()
        self.dfs(arr, tar, 0, [], res)
        return res
