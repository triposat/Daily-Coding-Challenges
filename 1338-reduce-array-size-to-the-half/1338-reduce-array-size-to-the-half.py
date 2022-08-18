class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hmap = Counter(arr)
        heap = list(-i for i in hmap.values())
        heapify(heap)
        # print(heap)
        cnt=0
        n=len(arr)//2
        ans=0
        while cnt<n:
            cnt+=-1*heappop(heap)
            # print(cnt)
            ans+=1
        return ans