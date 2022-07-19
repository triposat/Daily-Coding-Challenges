# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def countPaths(i, j, m, n):
#             if i == m-1 and j == n-1:
#                 return 1
#             if i >= m or j >= n:
#                 return 0
#             else:
#                 return countPaths(i+1, j, m, n)+countPaths(i, j+1, m, n)
#         return countPaths(0, 0, m, n)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def countPaths(i, j, m, n, dp):
#             if i == m-1 and j == n-1:
#                 return 1
#             if i >= m or j >= n:
#                 return 0
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             else:
#                 dp[i][j] = countPaths(i+1, j, m, n, dp) + \
#                     countPaths(i, j+1, m, n, dp)
#                 return dp[i][j]
#         dp = [[-1 for _ in range(n)] for _ in range(m)]
#         return countPaths(0, 0, m, n, dp)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = m-1
        res = 1
        for i in range(1, r+1):
            res = res*(N-r+i)//i
        return res
    