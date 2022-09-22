class Solution:
    def matchPlayersAndTrainers(self, p: List[int], q: List[int]) -> int:
        p.sort()
        q.sort()
        
        i=len(p)-1
        j=len(q)-1
        cnt=0
        while i>-1 and j>-1:
            if p[i]>q[j]:
                i-=1
            elif p[i]<=q[j]:
                cnt+=1
                j-=1
                i-=1
        return cnt
                
            