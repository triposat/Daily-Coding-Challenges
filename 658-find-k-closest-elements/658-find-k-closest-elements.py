class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        for i in range(len(arr)):
            res.append((abs(x-arr[i]), arr[i]))
        heapify(res)
        ans=[]
        while k>0:
            ans.append(heappop(res)[1])
            k-=1
        return sorted(ans)