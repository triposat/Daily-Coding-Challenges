class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        heap = []
        i=0
        while i<k:
            heappush(heap, (-1*nums[i], i))
            i+=1
        ans = []
        for end in range(k, len(nums)):
            ans.append(-1*heap[0][0])
            while heap and heap[0][1] <= start:
                heappop(heap)
            start += 1
            heappush(heap, (-1*nums[end], end))
            # print(heap, end)
        ans.append(-1*heap[0][0])
        return ans


# from heapq import *

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         H = []
#         ans = []
        
#         for i in range(k):
            
#             heappush(H,[-nums[i],i])
        
#         ans.append(-H[0][0])
        
#         for i in range(k,len(nums)):
#             print(H)
#             heappush(H,[-nums[i],i])
            
#             while H and i - H[0][1] >= k:
#                 heappop(H)
            
#             ans.append(-H[0][0])
        
#         return ans