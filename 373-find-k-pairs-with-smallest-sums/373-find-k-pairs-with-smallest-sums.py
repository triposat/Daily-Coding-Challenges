class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)

        def add(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, (nums1[i]+nums2[j], i, j))
        add(0, 0)
        pairs = []
        while heap and len(pairs) < k:
            _, i, j = heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            add(i, j+1)
            if j == 0:
                add(i+1, j)
        return pairs