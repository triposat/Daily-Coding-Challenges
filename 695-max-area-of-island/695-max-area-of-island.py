class Solution:
    def markAll(self, row, col, i, j, grid):
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        self.cnt += 1
        for u, v in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            self.markAll(row, col, i+u, j+v, grid)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                self.cnt = 0
                if grid[i][j] == 1:
                    self.markAll(row, col, i, j, grid)
                    res = max(res, self.cnt)
        return res