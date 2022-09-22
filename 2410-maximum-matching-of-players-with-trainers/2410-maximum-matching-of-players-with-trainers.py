class Solution:
    def matchPlayersAndTrainers(self, p: List[int], q: List[int]) -> int:
#         p.sort()
#         q.sort()
        
#         i=len(p)-1
#         j=len(q)-1
#         cnt=0
#         while i>-1 and j>-1:
#             if p[i]>q[j]:
#                 i-=1
#             elif p[i]<=q[j]:
#                 cnt+=1
#                 j-=1
#                 i-=1
#         return cnt
        p=list(map(lambda x: -1*x, p))
        q=list(map(lambda x: -1*x, q))
        heapify(p)
        heapify(q)
        cnt=0
        while p and q:
            p1=-1*p[0]
            q1=-1*q[0]
            if p1<=q1:
                cnt+=1
                heappop(p)
                heappop(q)
            else:
                heappop(p)
        return cnt