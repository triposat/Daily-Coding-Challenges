class Solution:
    def dfs(self, nums, path, temp):
        temp.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(nums, [], res)
        return res