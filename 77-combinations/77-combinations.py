class Solution:
    def dfs(self, nums, path, temp, k):
        if len(path)==k:
            temp.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], temp, k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        self.dfs(list(range(1, n+1)), [], res, k)
        return res