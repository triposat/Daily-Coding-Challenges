# Time: O(m*n*logk)
# Space: O(k)

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        heappush(heap, (mat[0][0], 0, 0))
        while k > 0:
            res, row, col = heappop(heap)
            if row == 0 and col+1 < len(mat):
                heappush(heap, (mat[row][col+1], row, col+1))
            if row+1 < len(mat):
                heappush(heap, (mat[row+1][col], row+1, col))
            k -= 1
        return res
