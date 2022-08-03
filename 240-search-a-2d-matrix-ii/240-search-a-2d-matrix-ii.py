class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        row = 0
        col = len(mat[0])-1
        while row < len(mat) and col >= 0:
            if mat[row][col] == tar:
                return True
            elif mat[row][col] < tar:
                row += 1
            else:
                col -= 1
        return False