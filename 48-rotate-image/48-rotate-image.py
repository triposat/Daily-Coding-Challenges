# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        m = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rotated[j][m-i-1] = mat[i][j]
        mat = [row[:] for row in rotated]

# Time: O(n^2)
# Space: O(1)
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat.reverse()
        print(mat)
        for i in range(len(mat)):
            for j in range(i+1, len(mat[i])):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
