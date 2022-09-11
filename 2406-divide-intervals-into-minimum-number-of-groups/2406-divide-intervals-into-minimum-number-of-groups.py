class Solution:
    def minGroups(self, inter: List[List[int]]) -> int:
        inter.sort()
        heap = []
        heapify(heap)
        for i, j in inter:
            if heap and heap[0] < i:
                heappop(heap)
            heappush(heap, j)
        return len(heap)