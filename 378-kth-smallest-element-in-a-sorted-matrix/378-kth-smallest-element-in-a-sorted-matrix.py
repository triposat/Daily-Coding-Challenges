class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                heappush(heap, -mat[row][col])
                if len(heap) > k:
                    heappop(heap)
        return -heappop(heap)

