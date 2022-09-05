class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        res = []

        def combina(nums, k, path):
            if len(path) == k:
                res.append((path))
                return
            for i in range(len(nums)):
                combina(nums[i+1:], k, path+[nums[i]])

        col = len(mat[0])
        ans = 0
        combina(list(range(0, col)), cols, [])
        for comb in res:
            tot = 0
            comb = set(comb)
            for row in mat:
                flag = True
                for i in range(col):
                    if row[i] and i not in comb:
                        flag = False
                        break
                if flag:
                    tot += 1
            ans = max(ans, tot)
        return ans